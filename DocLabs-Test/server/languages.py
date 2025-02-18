import subprocess



def execute_python(exename: str, filename: str, dependencies: list[str]) -> str:
    result = subprocess.run(["python", filename], capture_output=True, text=True)
    return result.stdout


def execute_cpp(exename: str, filename: str, dependencies: list[str]) -> str:
    
    compile_result = subprocess.run(["g++", "-o", exename, filename] + dependencies, capture_output=True, text=True)
    if compile_result.returncode != 0:
        return compile_result.stdout
    
    run_result = subprocess.run([f"./{exename}"], capture_output=True, text=True)
    return run_result.stdout


def execute_java(exename: str, filename: str, dependencies: list[str]) -> str:

    compile_result = subprocess.run(["javac", "-d", "java/out", filename] + dependencies, capture_output=True, text=True)
    if compile_result.returncode != 0:
        return compile_result.stdout
    
    package_result = subprocess.run("jar", "-cfm", exename, "mainifest.txt", "-C out .")
    if package_result.returncode != 0:
        return package_result.stdout
    
    run_result = subprocess.run(["java", "-jar", exename], capture_output=True, text=True)
    return run_result.stdout


