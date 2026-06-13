from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

ALGORITHM = os.getenv("ALGORITHM")

ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
)

TELEGRAM_BOT_TOKEN = os.getenv(
    "TELEGRAM_BOT_TOKEN"
)

TELEGRAM_CHAT_ID = os.getenv(
    "TELEGRAM_CHAT_ID"
)
DISCORD_WEBHOOK_URL = os.getenv(
    "DISCORD_WEBHOOK_URL"
)
DATABASE_URL = os.getenv("DATABASE_URL")

LINKEDIN_CLIENT_ID = os.getenv(
    "LINKEDIN_CLIENT_ID"
)

LINKEDIN_CLIENT_SECRET = os.getenv(
    "LINKEDIN_CLIENT_SECRET"
)
