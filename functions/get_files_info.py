import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        work_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(work_dir,directory))
        valid_target_path = os.path.commonpath([work_dir, target_dir]) == work_dir
        #print(work_dir)
        #print(target_dir)
        if not valid_target_path:
            return (f'  Error: Cannot list "{directory}" as it is outside the permitted working directory')
        if not os.path.isdir(target_dir):
            return (f'  Error: "{directory}" is not a directory')
        result = ""
        for file in os.listdir(target_dir):
            file_path = os.path.join(target_dir, file)
            file_size = os.path.getsize(file_path)
            is_dir = os.path.isdir(file_path)
            data = (f"  - {file}: file_size={file_size} bytes, is_dir={is_dir}")
            result += f"{"".join(data)}\n"
        return result
        #print(result)
        #print(os.listdir(work_dir))
        #return (f'Success: "{directory}" is within the working directory')
        #if os.path.isdir(target_dir):
    except Exception as e:
        return f"Error: {e}"
    
schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}