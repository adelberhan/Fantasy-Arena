from flask import (
    flash,
    redirect,
    render_template,
    request,
    url_for,session,
)
from utils.decorators import (
    guest_required,
    login_required,
)
 
from services.auth_service import authenticate_user

from services.auth_service import (
    create_user,
    username_exists,
)

from utils.validators import (
    validate_password,
    validate_username,
)

from . import auth_bp


@auth_bp.route("/register", methods=["GET", "POST"])
@guest_required
def register():

    if request.method == "POST":

        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        valid, message = validate_username(username)

        if not valid:
            flash(message, "danger")
            return redirect(url_for("auth.register"))

        if username_exists(username):
            flash(
                "Username already exists.",
                "danger",
            )
            return redirect(url_for("auth.register"))

        valid, message = validate_password(password)

        if not valid:
            flash(message, "danger")
            return redirect(url_for("auth.register"))

        if password != confirm_password:
            flash(
                "Passwords do not match.",
                "danger",
            )
            return redirect(url_for("auth.register"))

        create_user(username, password)

        flash(
            "Account created successfully.",
            "success",
        )

        return redirect(url_for("auth.login"))
    return render_template("auth/register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
@guest_required
def login():

    if request.method == "POST":

        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        user = authenticate_user(username, password)

        if not user:
            flash(
                "Invalid username or password.",
                "danger",
            )
            return redirect(url_for("auth.login"))

        session["user_id"] = user.id
        session["username"] = user.username

        flash(
            f"Welcome {user.username}!",
            "success",
        )

        return redirect(url_for("dashboard.home"))

    return render_template("auth/login.html")

@auth_bp.route("/logout")
@login_required
def logout():

    session.clear()

    flash(
        "Logged out successfully.",
        "success",
    )

    return redirect(
        url_for("landing.index")
    )