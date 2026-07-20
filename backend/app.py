from flask import Flask
from flask_cors import CORS

from config import Config
from database import db
import models
from routes.patient_routes import patient_bp
from routes.appointment_routes import appointment_bp
from routes.call_routes import call_bp
from routes.dashboard_routes import dashboard_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)


    CORS(app)

    db.init_app(app)

    app.register_blueprint(patient_bp)
    app.register_blueprint(appointment_bp)
    app.register_blueprint(call_bp)
    app.register_blueprint(dashboard_bp)


    @app.route("/")
    def home():
        return {
            "message": "Medical Scheduling API",
            "status": "running"
        }

    @app.route("/health")
    def health():
        return {"status": "ok"}

    return app


app = create_app()


if __name__ == "__main__":
    with app.app_context():
        from models import *
        db.create_all()

    app.run(debug=True)