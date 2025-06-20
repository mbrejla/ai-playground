import os
from os import path
from functions.check_path import check_path


def get_files_info(working_directory, directory=None):
    try:
        work_path = check_path(working_directory, directory)

        if not path.isdir(work_path):
            return f'Error: "{directory}" is not a directory'

        dir_contents = os.listdir(work_path)

        content_string = ""

        for entry in dir_contents:
            entry_abs = path.join(work_path, entry)
            is_dir = path.isdir(entry_abs)
            size = path.getsize(entry_abs)

            content_string += f"- {entry}: file_size={size}, is_dir={is_dir}\n"

        # print(work_path)
        return content_string
    except Exception as e:
        return f"Error: {e}"
