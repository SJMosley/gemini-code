import os

def get_files_info(working_directory, directory=None):
    if directory == None:
        # print(f"Error: {directory} is not a directory")
        return f'Error: "{directory}" is not a directory'
    if "../" in directory:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    abs_working_directory = os.path.abspath(working_directory)
    target_dir = os.path.join(abs_working_directory, directory)
    if not target_dir.startswith(abs_working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        # print(f"Error: {directory} is not a directory")
        return f'Error: "{directory}" is not a directory'
    file_info = []
    for item in os.listdir(target_dir):
        filepath = os.path.join(target_dir, item)
        is_dir = os.path.isdir(filepath)
        file_size = os.path.getsize(filepath)

        file_info.append(f"- {item}: file_size={file_size} bytes, is_dir={is_dir}")

    return "\n".join(file_info)
