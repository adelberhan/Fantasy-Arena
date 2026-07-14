from flask import Blueprint

rooms_bp = Blueprint(
    "rooms",
    __name__,
    url_prefix="/rooms",
    template_folder="../../templates/rooms",
)

from . import routes
