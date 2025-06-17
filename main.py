import os
import sys
from dotenv import load_dotenv
from google import genai
from functions.func_schemas import (
    schema_get_files_info,
    schema_get_file_content,
    schema_run_python,
    schema_write_file,
)
from functions.call_function import call_function

SYSTEM_PROMPT = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    model = "gemini-2.0-flash-001"

    verbose = False
    args = sys.argv[1:]

    if not args or args[0] == "" or args[0].startswith("--"):
        print(
            'Error: No correct prompt given.\nUsage: python3 main.py "Your prompt here." [--verbose]'
        )
        sys.exit(1)
    if "--verbose" in args:
        verbose = True

    prompt = args[0]
    available_functions = genai.types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python,
            schema_write_file,
        ]
    )
    messages = [
        genai.types.Content(role="user", parts=[genai.types.Part(text=prompt)]),
    ]
    answer_object = client.models.generate_content(
        model=model,
        contents=messages,
        config=genai.types.GenerateContentConfig(
            tools=[available_functions], system_instruction=SYSTEM_PROMPT
        ),
    )
    meta = answer_object.usage_metadata

    if answer_object.text:
        print(answer_object.text)
    if answer_object.function_calls:
        for call in answer_object.function_calls:
            call_function(call, True)
    if verbose:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {meta.prompt_token_count}")
        print(f"Response tokens: {meta.candidates_token_count}")


if __name__ == "__main__":
    main()
