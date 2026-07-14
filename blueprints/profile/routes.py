from flask import render_template

from . import profile_bp

@profile_bp.route("/profile")
def profile():
    return 'profile page'