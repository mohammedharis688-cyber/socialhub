import requests

from app.config import (
    DISCORD_WEBHOOK_URL
)


def send_message(text: str):

    payload = {
        "content": text
    }

    response = requests.post(
        DISCORD_WEBHOOK_URL,
        json=payload
    )

    return response.json() \
        if response.content else {
            "status": "sent"
        }
def send_file(file_path: str):

    with open(file_path, "rb") as file:

        response = requests.post(
            DISCORD_WEBHOOK_URL,
            files={
                "file": file
            }
        )

    return {
        "status": response.status_code
    }