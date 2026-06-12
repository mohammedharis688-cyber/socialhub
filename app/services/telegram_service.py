import requests
from app.config import (
    TELEGRAM_BOT_TOKEN,
    TELEGRAM_CHAT_ID
)

BOT_TOKEN = TELEGRAM_BOT_TOKEN
CHAT_ID = TELEGRAM_CHAT_ID

def send_message(text: str):

    url = (
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    )

    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }

    response = requests.post(
        url,
        json=payload
    )

    return response.json()
def send_document(file_path: str):

    url = (
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
    )

    with open(file_path, "rb") as document:

        response = requests.post(
            url,
            data={
                "chat_id": CHAT_ID
            },
            files={
                "document": document
            }
        )

    return response.json()
def send_photo(file_path: str):

    url = (
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    )

    with open(file_path, "rb") as photo:

        response = requests.post(
            url,
            data={
                "chat_id": CHAT_ID
            },
            files={
                "photo": photo
            }
        )

    return response.json()