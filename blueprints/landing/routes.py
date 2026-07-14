from flask import (
    redirect,
    render_template,
    session,
    url_for,
)

from . import landing_bp


@landing_bp.route("/")
def index():

    if "user_id" in session:

        return redirect(
            url_for("dashboard.home")
        )

    return render_template(
        "landing/index.html"
    )

# from flask import render_template

# from . import landing_bp


# @landing_bp.route("/")
# def index():

#     return render_template(
#         "landing/index.html"
#     )