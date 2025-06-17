import os
import subprocess

def run_python_file(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    # print(abs_working_directory)
    target_file = os.path.join(abs_working_directory, file_path)
    # print(target_file)
    if not target_file.startswith(abs_working_directory) or "../" in file_path:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(target_file):
        return f'Error: File "{file_path}" not found.'
    if not target_file.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        completed = subprocess.run(["python3", f"{file_path}"], capture_output=True, timeout=30, cwd=abs_working_directory)
        if len(str(completed.stdout)) == 0:
            return "No output produced."
        stdout_str = "\nSTDOUT:" + str(completed.stdout)
        stderr_str = "\nSTDERR:" + str(completed.stderr)
        return_code = f"\nProcess exited with code {completed.returncode}"
        output = stdout_str + stderr_str + return_code
        return output
    except Exception as e:
        print(f"Error: executing Python file: {e}")
        return f"Error: executing Python file: {e}"
