from flask import (
    flash,
    redirect,
    request,
    session,
    url_for,
)

from services.prediction_service import (
    submit_prediction_for_user,
)

from utils.decorators import login_required

from . import predictions_bp


@predictions_bp.route(
    "/<room_code>",
    methods=["POST"],
)
@login_required
def submit(room_code):
    saved, message, room = submit_prediction_for_user(
        room_code,
        session["user_id"],
        request.form,
    )

    if room is None:
        flash(message, "danger")
        return redirect(url_for("dashboard.home"))

    category = "success" if saved else "warning"
    flash(message, category)

    return redirect(url_for("rooms.details", room_code=room.room_code))
