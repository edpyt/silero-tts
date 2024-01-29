from fastapi import FastAPI

from src.presentation.controllers.silero import (
    fetch_all_available_data,
    save_speech_to_disk,
)


def setup_controllers(app: FastAPI) -> None:
    app.add_api_route("/speech", save_speech_to_disk, methods=["POST"])

    app.add_api_route("/data", fetch_all_available_data)
