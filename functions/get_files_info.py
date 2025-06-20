import os
from os import path
from functions.check_path import check_path


def get_files_info(working_directory, directory=None):
    try:
        # if not path.isdir(working_directory):
        # return f'Error: "{working_directory}" is not a valid directory'

        # base_path = path.abspath(working_directory)
        # if directory:
        # work_path = path.abspath(path.join(base_path, directory))
        # else:
        # work_path = base_path

        # if not work_path.startswith(base_path):
        # return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

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
