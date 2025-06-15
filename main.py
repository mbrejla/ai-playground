import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
model = "gemini-2.0-flash-001"

prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

answer_object = client.models.generate_content(model=model, contents=prompt)
meta = answer_object.usage_metadata


print(answer_object.text)
print(f"Prompt tokens: {meta.prompt_token_count}")
print(f"Response tokens: {meta.candidates_token_count}")
