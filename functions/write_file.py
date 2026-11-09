import os

def write_file (working_directory: str, file_path: str, content: str) -> str:
    try:
        work_dir = os.path.abspath(working_directory)
        path_file = os.path.normpath(os.path.join(work_dir,file_path))
        valid_target_path = os.path.commonpath([work_dir, path_file]) == work_dir
        if not valid_target_path:
            return (f'  Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        if os.path.isdir(path_file):
            return (f'Error: Cannot write to "{path_file}" as it is a directory')
        os.makedirs(working_directory, exist_ok=True)
        with open(path_file, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Write's or change's file's content inside directory",
        "parameters": {
            "type": "object",
            "properties": {
                "working_directory": {
                    "type": "string",
                    "description": "Path to the working directory",
                },
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to create or change content in"
                },
                "content": {
                    "type": "string", 
                    "description": "Content to write in file"
                },
            },
        },
    },
}