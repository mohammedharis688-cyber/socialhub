from app.providers.telegram import (
    TelegramProvider
)

from app.providers.discord import (
    DiscordProvider
)


def get_provider(platform: str):

    providers = {
        "telegram": TelegramProvider(),
        "discord": DiscordProvider()
    }

    return providers.get(platform)