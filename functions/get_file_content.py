import os
def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        work_dir = os.path.abspath(working_directory)
        path_file = os.path.normpath(os.path.join(work_dir,file_path))
        valid_target_path = os.path.commonpath([work_dir, path_file]) == work_dir
        if not valid_target_path:
            return (f'  Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        if not os.path.isfile(path_file):
            return (f'  Error: File not found or is not a regular file: "{file_path}"')
        with open(path_file, "r") as f:
           file_content = f.read(10000)
           if f.read(1):
               file_content += f'[...File "{file_path}" truncated at {10000} characters]'
        return file_content
    except Exception as e:
        return f"Error: {e}"

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Get's file content in range of last 10000 character's",
        "parameters": {
            "type": "object",
            "properties": {
                "working_directory": {
                    "type": "string",
                    "description": "Path of the working directory",
                },
                "file_path": {
                    "type": "string",
                    "description": "File path to read character's from, realative to working directory"
                },
            },
        },
    },
}