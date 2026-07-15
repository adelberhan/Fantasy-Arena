from config import Config

from models.prediction import Prediction

# from services.room_logger import log
from services.room_service import get_room_by_code, get_room_by_id, parse_score

from utils.helpers import generate_id
from utils.json_storage import (
    load_json,
    save_json,
)


def submit_prediction_for_user(room_code, user_id, form):
    """Validate and save a user's prediction for a room."""

    room = get_room_by_code(room_code)

    if room is None:
        return False, "Room not found.", None

    if room.prediction_closed():
        return False, "Prediction deadline has passed.", room

    home_prediction = parse_score(form.get("home_prediction"))
    away_prediction = parse_score(form.get("away_prediction"))

    if home_prediction is None or away_prediction is None:
        return False, "Predictions must be valid non-negative numbers.", room

    save_prediction(
        room.id,
        user_id,
        home_prediction,
        away_prediction,
    )

    return True, "Prediction saved successfully.", room


def get_prediction(room_id, user_id):
    """Return user prediction for a room."""

    predictions = load_json(Config.JSON_FILES["predictions"])

    for prediction in predictions:

        if prediction["room_id"] == room_id and prediction["user_id"] == user_id:
            return Prediction.from_dict(prediction)

    return None


def save_prediction(
    room_id,
    user_id,
    home_prediction,
    away_prediction,
):
    """Create or update prediction."""

    predictions = load_json(Config.JSON_FILES["predictions"])

    for prediction in predictions:

        if prediction["room_id"] == room_id and prediction["user_id"] == user_id:

            prediction["home_prediction"] = home_prediction
            prediction["away_prediction"] = away_prediction

            save_json(
                Config.JSON_FILES["predictions"],
                predictions,
            )

            room = get_room_by_id(room_id)

            # log(
            #     room.room_code,
            #     f"User {user_id} updated prediction.",
            # )

            return

    prediction = Prediction(
        id=generate_id(),
        room_id=room_id,
        user_id=user_id,
        home_prediction=home_prediction,
        away_prediction=away_prediction,
        earned_points=0,
    )

    predictions.append(prediction.to_dict())

    save_json(
        Config.JSON_FILES["predictions"],
        predictions,
    )

    room = get_room_by_id(room_id)

    # log(
    #     room.room_code,
    #     f"User {user_id} submitted prediction.",
    # )


def calculate_points(
    home_prediction,
    away_prediction,
    home_score,
    away_score,
):
    """Calculate earned points."""

    # Exact score
    if home_prediction == home_score and away_prediction == away_score:
        return 5

    # Predicted result
    if home_prediction > away_prediction:
        predicted_result = "home"

    elif home_prediction < away_prediction:
        predicted_result = "away"

    else:
        predicted_result = "draw"

    # Actual result
    if home_score > away_score:
        actual_result = "home"

    elif home_score < away_score:
        actual_result = "away"

    else:
        actual_result = "draw"

    if predicted_result == actual_result:

        if actual_result == "draw":
            return 1

        return 2

    return 0


def update_predictions_points(
    room_id,
    home_score,
    away_score,
):
    """Update all prediction and leaderboard points for a room."""

    predictions = load_json(Config.JSON_FILES["predictions"])

    updated_count = 0

    for prediction in predictions:

        if prediction["room_id"] != room_id:
            continue

        points = calculate_points(
            prediction["home_prediction"],
            prediction["away_prediction"],
            home_score,
            away_score,
        )

        prediction["earned_points"] = points

        updated_count += 1

    if updated_count:

        save_json(
            Config.JSON_FILES["predictions"],
            predictions,
        )

        room = get_room_by_id(room_id)

        # log(
        #     room.room_code,
        #     f"Points calculated for {updated_count} prediction(s).",
        # )

    return updated_count


def get_room_leaderboard(room_id):
    """Return leaderboard for a room based on user predictions."""

    predictions = load_json(Config.JSON_FILES["predictions"])
    users = load_json(Config.JSON_FILES["users"])

    leaderboard = []

    for pred in predictions:

        if pred["room_id"] != room_id:
            continue

        username = "Unknown user"

        for u in users:

            if u["id"] == pred["user_id"]:
                username = u["username"]
                break

        leaderboard.append({
            "username": username,
            "room_points": pred.get("earned_points", 0),
        })

    leaderboard.sort(
        key=lambda p: p.get("room_points", 0),
        reverse=True,
    )

    return leaderboard


def reset_prediction_points(room_id):
    """Reset all prediction points to 0 for a room."""

    predictions = load_json(Config.JSON_FILES["predictions"])

    updated = False

    for prediction in predictions:

        if prediction["room_id"] == room_id:

            prediction["earned_points"] = 0

            updated = True

    if updated:

        save_json(
            Config.JSON_FILES["predictions"],
            predictions,
        )

