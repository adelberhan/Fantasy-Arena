from config import Config

from utils.json_storage import load_json


def get_dashboard_statistics(user_id):
    """Return dashboard statistics for a user."""

    users = load_json(Config.JSON_FILES["users"])
    predictions = load_json(Config.JSON_FILES["predictions"])

    user = None
    for u in users:
        if u["id"] == user_id:
            user = u
            break  

    if user is None:
        return {
            "username": "Unknown user",
            "global_points": 0,
            "created_rooms": 0,
            "total_points": 0,
        }


    total_points = sum(
        prediction.get("earned_points", 0)
        for prediction in predictions
        if prediction["user_id"] == user_id
    )

    return {
        "username": user["username"],
        "global_points": user.get("global_points", 0),
        "total_points": total_points,
    }
