from functools import wraps

from flask import (
    flash,
    redirect,
    session,
    url_for,
)


def login_required(view):
    """Require login before accessing a page."""

    @wraps(view)
    def wrapped_view(*args, **kwargs):

        if "user_id" not in session:

            flash(
                "Please login first.",
                "warning",
            )

            return redirect(url_for("auth.login"))

        return view(*args, **kwargs)

    return wrapped_view


def guest_required(view):
    """Allow only guests."""

    @wraps(view)
    def wrapped_view(*args, **kwargs):

        if "user_id" in session:

            flash(
                "You are already logged in.",
                "info",
            )

            return redirect(url_for("dashboard.home"))

        return view(*args, **kwargs)

    return wrapped_view
