import os
import subprocess
def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        work_dir = os.path.abspath(working_directory)
        path_file = os.path.normpath(os.path.join(work_dir,file_path))
        valid_target_path = os.path.commonpath([work_dir, path_file]) == work_dir
        if not valid_target_path:
            return (f'  Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
        if not os.path.isfile(path_file):
            return (f'Error: "{file_path}" does not exist or is not a regular file')
        if not file_path.endswith(".py"):
            return (f'Error: "{file_path}" is not a Python file')
        command = ["python", path_file]
        if args:
            command.extend(args)
        finished_process = subprocess.run(command, capture_output=True, text=True, timeout=30, cwd=work_dir)
        result = ""
        if finished_process.returncode > 0:
            result += f"Process exited with code {finished_process.returncode}"
        if finished_process.stderr is None and finished_process.stdout is None:
            result += f"No output produced"
        result += f"STDOUT: {finished_process.stdout}\n"
        result += f"STDERR: {finished_process.stderr}"
        return result
    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Run's specified python file in directory",
        "parameters": {
            "type": "object",
            "properties": {
                "working_directory": {
                    "type": "string",
                    "description": "Path to the working directory",
                },
                "file_path": {
                    "type": "string",
                    "description": "path to the python file in working directory"
                },
                "args": {
                    "type": "array",
                    "description": "Additional arguments to running python file"
                },
            },
        },
    },
}
