from pathlib import Path
import secrets


BASE_DIR = Path(__file__).resolve().parent


class Config:
    SECRET_KEY = "football_prediction_secret_key"
    DATA_FOLDER = BASE_DIR / "data"
    # LOG_FOLDER = BASE_DIR / "logs"

    JSON_FILES = {
        "users": DATA_FOLDER / "users.json",
        "rooms": DATA_FOLDER / "rooms.json",
        "predictions": DATA_FOLDER / "predictions.json",
    }