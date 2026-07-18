from blueprints.auth import auth_bp
from blueprints.dashboard import dashboard_bp
from blueprints.landing import landing_bp
from blueprints.predictions import predictions_bp
from blueprints.profile import profile_bp
from blueprints.rooms import rooms_bp
from blueprints.leaderboard import leaderboard_bp


def register_blueprints(app):

    app.register_blueprint(landing_bp)

    app.register_blueprint(dashboard_bp)

    app.register_blueprint(auth_bp)

    app.register_blueprint(rooms_bp)

    app.register_blueprint(predictions_bp)

    app.register_blueprint(profile_bp)

    app.register_blueprint(leaderboard_bp)

