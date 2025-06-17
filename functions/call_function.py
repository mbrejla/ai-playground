from google.genai import types

from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.write_file import write_file

WORKING_DIRECTORY = "./calculator"
VALID_FUNCTIONS = {
    "get_file_content": get_file_content,
    "get_files_info": get_files_info,
    "run_python_file": run_python_file,
    "write_file": write_file,
}


def call_function(function_call, verbose=False):
    if verbose:
        print(f"Calling function: {function_call.name}({function_call.args})")
    else:
        print(f" - Calling function: {function_call.name}")
    if function_call.name not in VALID_FUNCTIONS:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call.name,
                    response={"error": f"Unknown function: {function_call.name}"},
                )
            ],
        )
    try:
        function_result = VALID_FUNCTIONS[function_call.name](
            WORKING_DIRECTORY, **function_call.args
        )
        # return function_result
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call.name,
                    response={"result": function_result},
                )
            ],
        )

    except Exception as e:
        return f'Error: Error running function: "{function_call.name}": {e}'
