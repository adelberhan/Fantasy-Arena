from pathlib import Path

from config import Config

from utils.helpers import current_timestamp


def log(room_code, message):
    """Write room activity."""

    log_file = Path(Config.LOG_FOLDER) / f"{room_code}.txt"

    with open(
        log_file,
        "a",
        encoding="utf-8",
    ) as file:

        file.write(
            f"[{current_timestamp()}] {message}\n"
        )


def get_room_logs(room_code):
    """Return newest room activity entries first."""

    log_file = Path(Config.LOG_FOLDER) / f"{room_code}.txt"

    if not log_file.exists():
        return []

    with open(
        log_file,
        "r",
        encoding="utf-8",
    ) as file:

        entries = [
            line.strip()
            for line in file
            if line.strip()
        ]

    entries.reverse()

    return entries
