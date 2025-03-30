from itertools import islice
import os

import program


USER_BUILD = "build"


class ContextError(Exception):
    def __init__(self, message: str):
        super().__init__(message)

class ExecutionError(Exception):
    def __init__(self, message: str):
        super().__init__(message)

class FileTypeError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class Environment:

    _EXTENSION_LANGUAGES = {
        ".h" : program.Language.CPP,
        ".hpp" : program.Language.CPP,
        ".cpp" : program.Language.CPP,
        ".java" : program.Language.JAVA,
        ".py" : program.Language.PYTHON,
    }

    def _get_file_language(filename: str):
        _, ext = os.path.splitext(filename)
        return Environment._EXTENSION_LANGUAGES.get(ext, program.Language.NONE)

    def __init__(self, user: str):
        self.__uid = user
        self.__executors = [
            program.get_executor(lang)(lang.name.lower(), USER_BUILD) for lang in program.Language
        ]
        self.__valid = False

    def __enter__(self):
        self.__valid = True
        self.__setup()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        os.chdir("../..")
        self.__valid = False

    def check_valid(self):
        if not self.__valid:
            raise ContextError(f"Environment {self.__uid} is not in a valid context. Ensure operation is within a with statement.")

    def __setup(self):
        # Make and navigate to user directory
        try:
            os.makedirs(self.__uid, exist_ok=True)
            os.chdir(self.__uid)
        except FileNotFoundError:
            print("Directory not found:", self.__uid)
            return False
        except Exception as e:
            print("An error occurred:", e)
            return False

        # Make language directories
        for lang in islice(program.Language, 1, None):
            os.makedirs(lang.name.lower(), exist_ok=True)
        os.makedirs(USER_BUILD, exist_ok=True)
        return True

    def destroy(self):
        self.check_valid()
        os.rmdir(".")

    def update_file(self, filename: str, content: str, overwrite: bool = True) -> bool:
        self.check_valid()
        # Validate language
        lang = Environment._get_file_language(filename)
        lang_dir = lang.name.lower()
        fullname = (
            os.path.join(USER_BUILD, filename)
            if lang == program.Language.NONE
            else os.path.join(lang_dir, filename)
        )
        if not overwrite and os.path.exists(fullname):
            return False
        
        with open(fullname, 'w') as file:
            file.write(content)
        return True

    def execute(
            self,
            exename: str,
            filename: str,
            dependencies: list[str]
        ) -> tuple[program.ExecutionResult, program.ExecutionResult]:
        self.check_valid()
        # Validate language
        lang = Environment._get_file_language(filename)
        if lang == program.Language.NONE:
            raise FileTypeError(f"File {filename} contains an unsupported language.")

        # Verify all dependencies are of the same language
        for dependency in dependencies:
            dep_lang = Environment._get_file_language(dependency)
            if dep_lang != lang:
                raise FileTypeError(f"Dependency {dependency} is not in the same language as target {filename}.")
        
        # Build program
        executor = self.__executors[lang.value]
        build_result = executor.build(exename, filename, dependencies)
        if build_result.return_code != 0:
            raise ExecutionError(f"Could not build program from {filename}:\n{build_result.message}")
        
        # Run executable
        run_result = executor.run(exename)
        if run_result.return_code != 0:
            raise ExecutionError(f"Could not execute program from {exename}:\n{run_result.message}")
        
        return build_result, run_result



