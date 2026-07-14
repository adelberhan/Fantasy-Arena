from . import rooms_bp
from flask import (
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from services.room_service import (
    create_room_for_user,
    delete_room_for_owner,
    get_all_rooms,
    get_room_by_code,
    save_result_for_owner,
    update_room_for_owner,
)
from services.room_logger import get_room_logs

from utils.decorators import login_required

from services.prediction_service import get_room_leaderboard, get_prediction


@rooms_bp.route("/")
def index():

    rooms = get_all_rooms()

    return render_template(
        "rooms/index.html",
        rooms=rooms,
    )


@rooms_bp.route("/create", methods=["GET", "POST"])
@login_required
def create():

    if request.method == "POST":

        valid, message, room = create_room_for_user(
            session["user_id"],
            request.form,
        )

        if not valid:
            flash(message, "danger")
            return redirect(url_for("rooms.create"))

        flash(
            message,
            "success",
        )

        return redirect(
            url_for(
                "rooms.details",
                room_code=room.room_code,
            )
        )

    return render_template("rooms/create.html")


@rooms_bp.route("/<room_code>")
@login_required
def details(room_code):

    room = get_room_by_code(room_code)

    if room is None:
        flash(
            "Room not found.",
            "danger",
        )

        return redirect(url_for("rooms.index"))

    leaderboard = get_room_leaderboard(room.id)
    existing_prediction = get_prediction(room.id, session["user_id"])
    activity_logs = get_room_logs(room.room_code)

    return render_template(
        "rooms/details.html",
        room=room,
        leaderboard=leaderboard,
        existing_prediction=existing_prediction,
        activity_logs=activity_logs,
    )
@rooms_bp.route(
    "/<room_code>/result",
    methods=["POST"],
)
@login_required
def result(room_code):

    saved, message, room = save_result_for_owner(
        room_code,
        session["user_id"],
        request.form,
    )

    if room is None:

        flash(
            message,
            "danger",
        )

        return redirect(url_for("dashboard.home"))

    flash(
        message,
        "success" if saved else "danger",
    )

    return redirect(
        url_for(
            "rooms.details",
            room_code=room.room_code,
        )
    )


@rooms_bp.route("/<room_code>/edit", methods=["GET", "POST"])
@login_required
def edit(room_code):

    room = get_room_by_code(room_code)

    if room is None:
        flash(
            "Room not found.",
            "danger",
        )

        return redirect(url_for("rooms.index"))

    if room.owner_id != session["user_id"]:
        flash(
            "Only the room owner can edit this room.",
            "danger",
        )

        return redirect(
            url_for(
                "rooms.details",
                room_code=room.room_code,
            )
        )

    if request.method == "POST":

        updated, message, room = update_room_for_owner(
            room_code,
            session["user_id"],
            request.form,
        )

        if not updated:
            flash(message, "danger")

            return render_template(
                "rooms/edit.html",
                room=room,
            )

        flash(
            message,
            "success",
        )

        return redirect(
            url_for(
                "rooms.details",
                room_code=room.room_code,
            )
        )

    return render_template(
        "rooms/edit.html",
        room=room,
    )


@rooms_bp.route("/<room_code>/delete", methods=["POST"])
@login_required
def delete(room_code):

    deleted, message, room = delete_room_for_owner(
        room_code,
        session["user_id"],
    )

    flash(
        message,
        "success" if deleted else "danger",
    )

    if deleted or room is None:
        return redirect(url_for("dashboard.home"))

    return redirect(
        url_for(
            "rooms.details",
            room_code=room.room_code,
        )
    )
