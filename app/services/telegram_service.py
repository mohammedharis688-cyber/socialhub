import requests
from app.config import (
    TELEGRAM_BOT_TOKEN,
    TELEGRAM_CHAT_ID
)

BOT_TOKEN = TELEGRAM_BOT_TOKEN
CHAT_ID = TELEGRAM_CHAT_ID

def send_message(text: str):
    try:
        url = (
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        )

        payload = {
            "chat_id": CHAT_ID,
            "text": text
        }

        response = requests.post(
            url,
            json=payload,
            timeout=10
        )

        return response.json()
    except Exception as e:

        return {
            "error": str(e)
        }
def send_document(file_path: str):
    try:
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
                },
                timeout=10
            )

        return response.json()
    except Exception as e:

        return {
            "error": str(e)
        }
def send_photo(file_path: str):
    try:
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
                },
                timeout=10
            )

        return response.json()
    except Exception as e:

        return {
            "error": str(e)
        }