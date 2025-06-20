import os
from os import path

from functions.check_path import check_path


def write_file(working_directory, file_path, content):
    try:
        file_path_abs = check_path(working_directory, file_path)
        directory = path.dirname(file_path_abs)
        if not path.exists(directory):
            os.makedirs(directory)

        with open(file_path_abs, "w") as file:
            file.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )

    except Exception as e:
        return f"Error: {e}"
