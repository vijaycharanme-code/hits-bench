import os
from pathlib import Path

def list_files(directory: str) -> list:
    path = Path(directory)
    if path.exists() and path.is_dir():
        return [str(p) for p in path.iterdir()]
    return []

def read_file(file_path: str) -> str:
    path = Path(file_path)
    if path.exists() and path.is_file():
        try:
            return path.read_text()
        except Exception:
            return ""
    return ""
