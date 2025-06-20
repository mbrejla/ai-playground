import os
from os import path

from functions.check_path import check_path
from settings import MAX_BYTES


def get_file_content(working_directory, file_path):
    try:
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
