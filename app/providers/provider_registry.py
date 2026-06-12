from app.providers.telegram import (
    TelegramProvider
)


def get_provider(platform: str):

    providers = {
        "telegram": TelegramProvider()
    }

    return providers.get(platform)