import json
import os
from pathlib import Path
from tempfile import NamedTemporaryFile


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

    try:
        with open(
            file_path,
            "r",
            encoding="utf-8",
        ) as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_json(file_path, data):
    """Save data to a JSON file atomically."""

    file_path = Path(file_path)

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
