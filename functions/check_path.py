import os
from os import path


def check_path(working_directory, directory=None):
    try:
        if not path.isdir(working_directory):
            raise Exception(f'"{working_directory}" is not a valid directory')

        base_path = path.abspath(working_directory)
        if directory:
            work_path = path.abspath(path.join(base_path, directory))
        else:
            work_path = base_path

        if not work_path.startswith(base_path):
            raise Exception(
                # will fail one boot.dev cli test because 'execute' is expected instead of access
                f'Cannot access "{directory}" as it is outside the permitted working directory'
            )
        return work_path
    except Exception as e:
        raise Exception(e)
