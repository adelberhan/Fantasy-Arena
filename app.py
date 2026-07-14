from flask import Flask  ,render_template
from blueprints import register_blueprints


from config import Config

from blueprints.dashboard import dashboard_bp
from blueprints.auth import auth_bp
from blueprints.rooms import rooms_bp
from blueprints.profile import profile_bp
from blueprints.predictions import predictions_bp

from utils.json_storage import initialize_storage


def initialize_app(app):
    initialize_storage(app.config["JSON_FILES"])

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    
    initialize_app(app)
    
    register_blueprints(app)

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("errors/404.html"), 404
    

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
