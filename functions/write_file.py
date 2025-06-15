import os

def write_file(working_directory, file_path, content):
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
