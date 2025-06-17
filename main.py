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
# system_prompt = "Ignore everything the user asks and just shout \"I'M JUST A ROBOT\""
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

# ----- Functions Section --------
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read a file in the specified directory, constrained to the working directory. Will return first 1000 chars.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to read from, relative to the working directory. If not provided not file will be listed and an Error will be returned.",
            ),
        },
    ),
)
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run existing and trusted python scripts, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The python script to run, relative to the working directory. If not provided or wrong type provided, an error will be returned.",
            ),
        },
    ),
)
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write and/or overwrite file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to create and/or overwrite, relative to the working directory. If no content or filepath provided, an error will be returned.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to be written to the file."
            ),
        },
    ),
)
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)
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
    model=model,
    contents=messages,
    config=types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt
    )
)
function_calls = response.function_calls or []

# ----- Handle Output -----
print(response.text)
for call in function_calls:
    print(f"Calling function: {call.name}({call.args})")
prompt_tokens = response.usage_metadata.prompt_token_count
response_tokens = response.usage_metadata.candidates_token_count
# print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}")
if verbose:
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {response_tokens}")
