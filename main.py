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
from settings import MAX_TRIES, SYSTEM_PROMPT


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    model = "gemini-2.0-flash-001"

    args = sys.argv[1:]

    if not args or args[0] == "" or args[0].startswith("--"):
        print(
            'Error: No correct prompt given.\nUsage: python3 main.py "Your prompt here." [--verbose]'
        )
        sys.exit(1)
    verbose = "--verbose" in args
    debugging = "--debug" in args

    prompt = args[0]
    available_functions = genai.types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python,
            schema_write_file,
        ]
    )

    # start a new conversation with the given prompt (role:user)
    messages = [
        genai.types.Content(role="user", parts=[genai.types.Part(text=prompt)]),
    ]

    loop_try = 0
    while loop_try <= MAX_TRIES:
        loop_try += 1
        print(f"\nLoop: {loop_try} ***")
        answer_object = client.models.generate_content(
            model=model,
            contents=messages,
            config=genai.types.GenerateContentConfig(
                tools=[available_functions], system_instruction=SYSTEM_PROMPT
            ),
        )
        meta = answer_object.usage_metadata

        # get all response candidates and add them to the conversation (role:model)
        for item in answer_object.candidates:
            messages.append(item.content)

        # if we get function calls, hand them over and check the results for a response
        # also add the complete function_call result to the conversation (role:tool)
        if answer_object.function_calls:
            for call in answer_object.function_calls:
                result = call_function(call, verbose)
                if not result.parts[0].function_response.response:
                    raise Exception(f"FATAL!: Call to {call} didn't return a result.")
                messages.append(result)
                if verbose:
                    print(f"-> {result.parts[0].function_response.response}")

            # loop ends here ?
        else:
            # print the textresponse, if we got one
            if answer_object.text:
                print(answer_object.text)
            break

    if verbose:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {meta.prompt_token_count}")
        print(f"Response tokens: {meta.candidates_token_count}")
    if debugging:
        print("**********************")
        print(messages)
        print("**********************")


if __name__ == "__main__":
    main()
