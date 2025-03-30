from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from os import path
import os
import subprocess


class Language(Enum):
    NONE = 0
    CPP = 1
    JAVA = 2
    PYTHON = 3


@dataclass
class ExecutionResult:
    message: str
    return_code: int


class ProgramExecutor(ABC):

    def __init__(self, source_path: str, build_path: str):
        self._source_path = source_path
        self._build_path = build_path


    @abstractmethod
    def build(
        self,
        exename: str,
        filename: str,
        dependencies: list[str]
    ) -> ExecutionResult:
        pass

    @abstractmethod
    def run(
        self,
        exename: str,
        args: str = ""
    ) -> ExecutionResult:
        pass


class NullExecutor(ProgramExecutor):

    LANG = Language.NONE

    def __init__(self, source_path: str, build_path: str):
        super().__init__(source_path, build_path)

    def build(
        self,
        exename: str,
        filename: str,
        dependencies: list[str]
    ) -> ExecutionResult:
        return ExecutionResult("", 0)

    def run(
        self,
        exename: str,
        args: str = ""
    ) -> ExecutionResult:
        return ExecutionResult("", 0)


class CppExecutor(ProgramExecutor):

    LANG = Language.CPP

    def __init__(self, source_path: str, build_path: str):
        super().__init__(source_path, build_path)

    def build(
        self,
        exename: str,
        filename: str,
        dependencies: list[str]
    ) -> ExecutionResult:
        exepath = path.join(self._build_path, exename)
        filepath = path.join(self._source_path, filename)
        dependency_paths = [path.join(self._source_path, dependency) for dependency in dependencies]

        result = subprocess.run(
            ["g++", "-o", exepath, filepath] + dependency_paths,
            capture_output=True,
            text=True
        )
        return ExecutionResult(result.stdout, result.returncode)

    def run(
        self,
        exename: str,
        args: str = ""
    ) -> ExecutionResult:
        #exepath = path.join(self._build_path, exename)
        os.chdir(self._build_path)
        result = subprocess.run(
            [f"./{exename}"],
            capture_output=True,
            text=True,
            input=args
        )
        os.chdir("..")
        return ExecutionResult(result.stdout, result.returncode)


class JavaExecutor(ProgramExecutor):

    LANG = Language.JAVA

    def __init__(self, source_path: str, build_path: str):
        super().__init__(source_path, build_path)

    def build(
        self,
        exename: str,
        filename: str,
        dependencies: list[str]
    ) -> ExecutionResult:
        exepath = path.join(self._build_path, exename)
        filepath = path.join(self._source_path, filename)
        dependency_paths = [path.join(self._source_path, dependency) for dependency in dependencies]

        compile_result = subprocess.run(
            ["javac", "-d", "java/out", filepath] + dependency_paths,
            capture_output=True,
            text=True
        )
        if compile_result.returncode != 0:
            return ExecutionResult(compile_result.stdout, compile_result.returncode)
        
        package_result = subprocess.run(
            "jar",
            "-cfm",
            exepath,
            "manifest.txt",
            "-C out ."
        )
        return ExecutionResult(package_result.stdout, package_result.returncode)

    def run(
        self,
        exename: str,
        args: str = ""
    ) -> ExecutionResult:
        exepath = path.join(self._build_path, exename)
        result = subprocess.run(
            ["java", "-jar", exepath],
            capture_output=True,
            text=True,
            input=args
        )
        return ExecutionResult(result.stdout, result.returncode)


_PYTHON_HEADER = (
"""# ================================ PYTHON HEADER ================================= #
import os
import sys

module_dir = os.path.join(os.path.dirname(__file__), "../python")
sys.path.append(module_dir)
os.chdir("build")
del module_dir
# ================================================================================ #
""")

class PythonExecutor(ProgramExecutor):

    LANG = Language.PYTHON

    def __init__(self, source_path: str, build_path: str):
        super().__init__(source_path, build_path)

    def build(
        self,
        exename: str,
        filename: str,
        dependencies: list[str]
    ) -> ExecutionResult:
        exepath = path.join(self._build_path, exename)
        filepath = path.join(self._source_path, filename)

        content = None
        with open(filepath, "r") as infile:
            content = infile.read()

        with open(exepath, "w") as outfile:
            outfile.write(_PYTHON_HEADER)
            outfile.write(content)

        return ExecutionResult("", 0)

    def run(
        self,
        exename: str,
        args: str = ""
    ) -> ExecutionResult:
        exepath = path.join(self._build_path, exename)
        print(f"Base path: {os.path.abspath('.')}")
        print(f"exepath: {exepath}")
        result = subprocess.run(
            ["python3", exepath],
            capture_output=True,
            text=True,
            input=args
        )
        return ExecutionResult(result.stdout, result.returncode)


_EXECUTORS = [NullExecutor, CppExecutor, JavaExecutor, PythonExecutor]

def get_executor(lang: Language) -> ProgramExecutor:
    return _EXECUTORS[lang.value]
