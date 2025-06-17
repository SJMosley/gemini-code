import os
from google.genai import types

def write_file(working_directory, file_path, content):
    if len(content) == 0:
        return "Error: no content provided to write to file"
    abs_working_directory = os.path.abspath(working_directory)
    # print(abs_working_directory)
    target_file = os.path.join(abs_working_directory, file_path)
    # print(target_file)
    if not target_file.startswith(abs_working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    #Make Dirs
    new_path, _ = target_file.rsplit("/", 1)
    if not os.path.exists(new_path):
        os.makedirs(new_path)


    try:
        with open(target_file, "w") as f:
            f.write(content)
    except (IOError, OSError):
        print(f"Error: writing to file {file_path}")

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

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
