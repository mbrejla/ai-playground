import os
from os import path

from functions.check_path import check_path

MAX_BYTES = 10000


def get_file_content(working_directory, file_path):
    try:
        # if not path.isdir(working_directory):
        #     return f'Error: "{working_directory}" is not a valid directory'
        #
        # base_path_abs = path.abspath(working_directory)
        # file_path_abs = path.abspath(path.join(base_path_abs, file_path))
        #
        # if not file_path_abs.startswith(base_path_abs):
        #     return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        file_path_abs = check_path(working_directory, file_path)

        if not path.isfile(file_path_abs):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        oversize = path.getsize(file_path_abs) > MAX_BYTES

        with open(file_path_abs, "r") as file:
            contents = file.read(MAX_BYTES)

        if oversize:
            contents += f'\n[...File "{file_path}" truncated at 10000 characters]'
        return contents

    except Exception as e:
        return f"Error: {e}"
