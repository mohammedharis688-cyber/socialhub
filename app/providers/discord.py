from app.services.discord_service import (
    send_message,
    send_file
)


class DiscordProvider:

    def publish(self, post):

        send_message(
            post.content
        )

        for media in post.media:

            send_file(
                media.file_url
            )

        return {
            "message": "Published to Discord"
        }