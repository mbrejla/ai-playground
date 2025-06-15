import os
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
model = "gemini-2.0-flash-001"

verbose = False

if len(sys.argv) <= 1:
    print('Error: No prompt given.\nUsage: python3 main.py "Your prompt here."')
    sys.exit(1)
if not isinstance(sys.argv[1], str) or sys.argv[1].startswith("--"):
    print("Error: Prompt must be the first parameter")
    sys.exit(1)

if "--verbose" in sys.argv:
    verbose = True

prompt = sys.argv[1]
messages = [
    genai.types.Content(role="user", parts=[genai.types.Part(text=prompt)]),
]
answer_object = client.models.generate_content(model=model, contents=messages)
meta = answer_object.usage_metadata


print(answer_object.text)
if verbose:
    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {meta.prompt_token_count}")
    print(f"Response tokens: {meta.candidates_token_count}")
