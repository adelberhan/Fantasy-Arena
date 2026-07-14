from flask import (
    render_template,
    session,
)

from services.dashboard_service import (
    get_dashboard_statistics,
)
from services.room_service import get_all_rooms

from utils.decorators import login_required

from . import dashboard_bp


@dashboard_bp.route("/dashboard")
@login_required
def home():

    statistics = get_dashboard_statistics(
        session["user_id"]
    )

    rooms = get_all_rooms()

    return render_template(
        "dashboard/index.html",
        statistics=statistics,
        rooms=rooms,
    )
