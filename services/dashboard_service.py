from config import Config

from utils.json_storage import load_json


def get_dashboard_statistics(user_id):
    """Return dashboard statistics for a user."""

    users = load_json(Config.JSON_FILES["users"])
    rooms = load_json(Config.JSON_FILES["rooms"])
    predictions = load_json(Config.JSON_FILES["predictions"])

    user = next(
        (user for user in users if user["id"] == user_id),
        None,
    )

    if user is None:
        return {
            "username": "Unknown user",
            "global_points": 0,
            "created_rooms": 0,
            "joined_rooms": 0,
            "total_points": 0,
        }

    created_rooms = sum(
        room["owner_id"] == user_id
        for room in rooms
    )

    joined_rooms = sum(
        prediction["user_id"] == user_id
        for prediction in predictions
    )

    total_points = sum(
        prediction.get("earned_points", 0)
        for prediction in predictions
        if prediction["user_id"] == user_id
    )

    return {
        "username": user["username"],
        "global_points": user.get("global_points", 0),
        "created_rooms": created_rooms,
        "joined_rooms": joined_rooms,
        "total_points": total_points,
    }
