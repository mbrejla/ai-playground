import os
import subprocess
from os import path
from functions.check_path import check_path


def run_python_file(working_directory, file_path):
    try:
        file_path_abs = check_path(working_directory, file_path)
        working_dir_abs = check_path(working_directory)
        if not path.exists(file_path_abs):
            return f'Error: File "{file_path}" not found.'
        if not path.isfile(file_path_abs) or path.splitext(file_path_abs)[1] != ".py":
            return f'Error: "{file_path}" is not a Python file.'

        result = subprocess.run(
            ["python3", file_path_abs],
            timeout=30,
            cwd=working_dir_abs,
            capture_output=True,
            text=True,
        )

        result_out = ""

        if result.stdout:
            result_out = f"STDOUT:\n{result.stdout}\n"
        else:
            result_out = "No Output produced.\n"
        if result.stderr:
            result_out += f"STDERR:\n{result.stderr}\n"
        if result.returncode:
            result_out += f"Process exited with code {result.returncode}"

        return result_out

    except Exception as e:
        return f"Error: {e}"
