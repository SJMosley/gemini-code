# ----- Setup -----
import os
import sys
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai
from google.genai import types

client = genai.Client(api_key=api_key)
model = "gemini-2.0-flash-001"
# ----- Process Args -----

verbose = "--verbose" in sys.argv
if len(sys.argv) < 2:
    print("YIKES! You have to add a prompt! 🤦‍♂️")
    sys.exit(1)

user_prompt = sys.argv[1]

# ----- Call LLM -----
messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

response = client.models.generate_content(
    model=model, contents=messages
)

# ----- Handle Output -----
print(response.text)
prompt_tokens = response.usage_metadata.prompt_token_count
response_tokens = response.usage_metadata.candidates_token_count
# print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}")
if verbose:
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {response_tokens}")
