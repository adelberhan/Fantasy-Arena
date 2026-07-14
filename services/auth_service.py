from config import Config

from models.user import User

from utils.helpers import (
    current_timestamp,
    generate_id,
)

from utils.json_storage import (
    load_json,
    save_json,
)


def username_exists(username):
    """Return True if username already exists."""

    users = load_json(Config.JSON_FILES["users"])

    return any(user["username"].lower() == username.lower() for user in users)


def create_user(username, password):
    """Create a new user."""

    users = load_json(Config.JSON_FILES["users"])

    user = User(
        id=generate_id(),
        username=username,
        password=User.hash_password(password),
        created_at=current_timestamp(),
        updated_at=current_timestamp(),
    )

    users.append(user.to_dict())

    save_json(
        Config.JSON_FILES["users"],
        users,
    )


    return user

def find_user_by_username(username):
    """Return a User object by username or None."""

    users = load_json(Config.JSON_FILES["users"])

    for user_data in users:
        if user_data["username"].lower() == username.lower():
            return User.from_dict(user_data)

    return None

def authenticate_user(username, password):
    """Authenticate a user."""

    user = find_user_by_username(username)

    if not user:
        return None

    if not user.verify_password(password):
        return None

    return user