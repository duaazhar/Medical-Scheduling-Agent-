from flask import Flask
from flask_cors import CORS

from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)

    @app.route("/")
    def home():
        return {
            "message": "Medical Scheduling API",
            "status": "running"
        }

    @app.route("/health")
    def health():
        return {
            "status": "ok"
        }

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)