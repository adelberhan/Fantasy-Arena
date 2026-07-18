from config import Config

from models.room import Room

# from services.room_logger import log

from utils.helpers import (
    current_timestamp,
    generate_id,
    generate_room_code,
    parse_match_datetime,
)

from utils.json_storage import (
    load_json,
    save_json,
)
from utils.validators import (
    validate_room_name,
    validate_team_name,
)


def parse_score(value):
    """Return a non-negative score or None."""

    try:
        score = int(value)
    except (TypeError, ValueError):
        return None

    if score < 0:
        return None

    return score


def create_room_for_user(user_id, form):
    """Validate form data and create a room for the current user."""

    valid, message, room_data = validate_room_form(form)

    if not valid:
        return False, message, None

    room = create_room(
        owner_id=user_id,
        room_name=room_data["room_name"],
        home_team=room_data["home_team"],
        away_team=room_data["away_team"],
        home_logo=room_data["home_logo"],
        away_logo=room_data["away_logo"],
        match_datetime=room_data["match_datetime"],
    )

    return True, "Room created successfully.", room


def validate_room_form(form):
    """Validate shared room form fields."""

    room_name = form.get("room_name", "").strip()
    home_team = form.get("home_team", "").strip()
    away_team = form.get("away_team", "").strip()

    valid, message = validate_room_name(room_name)

    if not valid:
        return False, message, None

    valid, message = validate_team_name(home_team)

    if not valid:
        return False, message, None

    valid, message = validate_team_name(away_team)

    if not valid:
        return False, message, None

    try:
        match_datetime = parse_match_datetime(
            form.get("match_date"),
            form.get("match_time"),
        )
    except (TypeError, ValueError):
        return False, "Match date or time is invalid.", None

    return (
        True,
        "",
        {
            "room_name": room_name,
            "home_team": home_team,
            "away_team": away_team,
            "home_logo": form.get("home_logo", "").strip(),
            "away_logo": form.get("away_logo", "").strip(),
            "match_datetime": match_datetime,
        },
    )


def create_room(
    owner_id,
    room_name,
    home_team,
    away_team,
    home_logo,
    away_logo,
    match_datetime,
):
    """Create a new room."""

    rooms = load_json(Config.JSON_FILES["rooms"])

    room = Room(
        id=generate_id(),
        room_name=room_name,
        room_code=generate_room_code(),
        owner_id=owner_id,
        home_team=home_team,
        away_team=away_team,
        home_logo=home_logo,
        away_logo=away_logo,
        match_datetime=match_datetime,
        deadline=Room.calculate_deadline(match_datetime),
        home_score=None,
        away_score=None,
        created_at=current_timestamp(),
        updated_at=current_timestamp(),
    )

    rooms.append(room.to_dict())

    save_json(
        Config.JSON_FILES["rooms"],
        rooms,
    )

    return room


def get_room_by_code(room_code):
    """Return room by code."""

    rooms = load_json(Config.JSON_FILES["rooms"])

    for room in rooms:
        if room["room_code"] == room_code:
            return Room.from_dict(room)

    return None


def user_owns_room(room, user_id):
    """Return True when the user owns the room."""

    return room is not None and room.owner_id == user_id


def update_room_for_owner(room_code, user_id, form):
    """Update room details when the user owns the room."""

    room = get_room_by_code(room_code)

    if room is None:
        return False, "Room not found.", None

    if not user_owns_room(room, user_id):
        return False, "Only the room owner can edit this room.", room

    valid, message, room_data = validate_room_form(form)

    if not valid:
        return False, message, room

    rooms = load_json(Config.JSON_FILES["rooms"])

    for saved_room in rooms:

        if saved_room["room_code"] == room_code:

            new_deadline = Room.calculate_deadline(room_data["match_datetime"])
            deadline_changed = saved_room.get("deadline") != new_deadline

            saved_room["room_name"] = room_data["room_name"]
            saved_room["home_team"] = room_data["home_team"]
            saved_room["away_team"] = room_data["away_team"]
            saved_room["home_logo"] = room_data["home_logo"]
            saved_room["away_logo"] = room_data["away_logo"]
            saved_room["match_datetime"] = room_data["match_datetime"]
            saved_room["deadline"] = new_deadline
            saved_room["updated_at"] = current_timestamp()

            if deadline_changed:
                saved_room["home_score"] = None
                saved_room["away_score"] = None

                from services.prediction_service import reset_prediction_points

                reset_prediction_points(saved_room["id"])

            save_json(
                Config.JSON_FILES["rooms"],
                rooms,
            )

            # log(room_code, "Room details updated.")

            return True, "Room updated successfully.", Room.from_dict(saved_room)

    return False, "Room not found.", None


def delete_room_for_owner(room_code, user_id):
    """Delete a room when the user owns it."""

    room = get_room_by_code(room_code)

    if room is None:
        return False, "Room not found.", None

    if not user_owns_room(room, user_id):
        return False, "Only the room owner can delete this room.", room

    rooms = load_json(Config.JSON_FILES["rooms"])
    predictions = load_json(Config.JSON_FILES["predictions"])

    rooms = [saved_room for saved_room in rooms if saved_room["room_code"] != room_code]

    predictions = [
        prediction for prediction in predictions if prediction["room_id"] != room.id
    ]

    save_json(
        Config.JSON_FILES["rooms"],
        rooms,
    )
    save_json(
        Config.JSON_FILES["predictions"],
        predictions,
    )

    # log(room_code, "Room deleted.")

    return True, "Room deleted successfully.", room


def save_match_result(
    room_code,
    home_score,
    away_score,
):
    """Save match result."""

    rooms = load_json(Config.JSON_FILES["rooms"])

    for room in rooms:

        if room["room_code"] == room_code:

            if room["home_score"] is not None or room["away_score"] is not None:
                return False

            room["home_score"] = home_score
            room["away_score"] = away_score
            room["updated_at"] = current_timestamp()

            save_json(
                Config.JSON_FILES["rooms"],
                rooms,
            )

            # log(room_code, f"Final result: {home_score}-{away_score}")

            return True

    return False


def save_result_for_owner(room_code, user_id, form):
    """Validate and save a match result when the user owns the room."""

    room = get_room_by_code(room_code)

    if room is None:
        return False, "Room not found.", None

    if room.owner_id != user_id:
        return False, "Only the room owner can add the result.", room

    if not room.match_ended():
        return False, "The match has not ended yet.", room

    if room.home_score is not None or room.away_score is not None:
        return False, "Match result has already been saved.", room

    home_score = parse_score(form.get("home_score"))
    away_score = parse_score(form.get("away_score"))

    if home_score is None or away_score is None:
        return False, "Scores must be valid non-negative numbers.", room

    saved = save_match_result(
        room.room_code,
        home_score,
        away_score,
    )

    if not saved:
        return False, "Match result could not be saved.", room

    from services.prediction_service import update_predictions_points

    update_predictions_points(
        room.id,
        home_score,
        away_score,
    )

    updated_room = get_room_by_code(room_code)

    return True, "Match result saved.", updated_room


def get_room_by_id(room_id):
    """Return room by id."""

    rooms = load_json(Config.JSON_FILES["rooms"])

    for room in rooms:

        if room["id"] == room_id:
            return Room.from_dict(room)

    return None


def get_all_rooms():
    """Return all rooms."""

    rooms = load_json(Config.JSON_FILES["rooms"])

    return [Room.from_dict(room) for room in rooms]
