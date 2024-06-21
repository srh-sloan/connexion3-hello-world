from connexion import FlaskApp
from pathlib import Path

def create_app():
    app = FlaskApp(__name__)

    app.add_api("api.yml")
    return app

app = create_app()
if __name__ == "__main__":
    app.run(f"{Path(__file__).stem}:app", port=8080)