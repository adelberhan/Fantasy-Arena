from datetime import datetime
import uuid
import secrets


def generate_id():
    """Generate a unique ID."""

    return uuid.uuid4().hex


def current_timestamp():
    """Return current timestamp."""

    return datetime.now().isoformat(timespec="seconds")


def generate_room_code():
    """Generate room code."""

    return secrets.token_hex(3).upper()


def parse_match_datetime(match_date, match_time):
    """Combine date and time into ISO format."""

    return datetime.fromisoformat(f"{match_date}T{match_time}").isoformat(
        timespec="minutes"
    )
