from app.providers.telegram import TelegramProvider
from app.providers.discord import DiscordProvider
from app.providers.linkedin import LinkedInProvider
from app.providers.facebook import (FacebookProvider)

def get_provider(platform: str):

    providers = {
        "telegram": TelegramProvider(),
        "discord": DiscordProvider(),
        "linkedin": LinkedInProvider(),
        "facebook": FacebookProvider()
    }

    return providers.get(platform)