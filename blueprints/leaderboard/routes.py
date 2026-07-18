from flask import render_template
from services.prediction_service import get_global_leaderboard
from . import leaderboard_bp


@leaderboard_bp.route("/leaderboard")
def leaderboard():
    leaderboard_data = get_global_leaderboard()
    return render_template("leaderboard.html", leaderboard=leaderboard_data)
