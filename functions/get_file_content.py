import os
from google.genai import types

def get_file_content(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    # print(abs_working_directory)
    target_file = os.path.join(abs_working_directory, file_path)
    # print(target_file)
    if not target_file.startswith(abs_working_directory):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    # print(f"target_dir: {os.path.isfile(target_file)}")
    # print(f"file_path: {os.path.isfile(file_path)}")
    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    #Read File
    MAX_CHARS = 10000

    try:
        with open(target_file, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string) == MAX_CHARS:
                file_content_string += f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'

    except Exception as e:
            return f"Error: could not read file content {e}"

    return file_content_string
    #[...File "{file_path}" truncated at 10000 characters]

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
