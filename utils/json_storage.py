import json
import os
from pathlib import Path
from tempfile import NamedTemporaryFile

if os.name == "nt":
    import msvcrt


class FileLock:
    """Small cross-process lock for JSON file access."""

    def __init__(self, file_path):
        self.lock_path = Path(f"{file_path}.lock")
        self.lock_file = None

    def __enter__(self):
        self.lock_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )
        self.lock_file = open(
            self.lock_path,
            "a+",
            encoding="utf-8",
        )

        if os.name == "nt":
            msvcrt.locking(
                self.lock_file.fileno(),
                msvcrt.LK_LOCK,
                1,
            )

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if os.name == "nt":
            self.lock_file.seek(0)
            msvcrt.locking(
                self.lock_file.fileno(),
                msvcrt.LK_UNLCK,
                1,
            )

        self.lock_file.close()


def initialize_storage(json_files):
    """Create JSON files if they do not exist."""

    for file_path in json_files.values():

        Path(file_path).parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        if not Path(file_path).exists():

            with open(
                file_path,
                "w",
                encoding="utf-8",
            ) as file:

                json.dump([], file, indent=4)


def load_json(file_path):
    """Load data from a JSON file."""

    with FileLock(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return json.load(file)

        except (FileNotFoundError, json.JSONDecodeError):
            return []


def save_json(file_path, data):
    """Save data to a JSON file atomically."""

    file_path = Path(file_path)

    with FileLock(file_path):
        file_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with NamedTemporaryFile(
            "w",
            encoding="utf-8",
            dir=file_path.parent,
            delete=False,
        ) as file:
            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False,
            )
            temp_path = file.name

        os.replace(
            temp_path,
            file_path,
        )
