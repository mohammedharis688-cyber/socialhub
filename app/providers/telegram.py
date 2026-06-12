from app.services.telegram_service import (
    send_message,
    send_document,
    send_photo
)


class TelegramProvider:

    def publish(self, post):

        send_message(post.content)

        for media in post.media:

            if media.media_type == "document":

                send_document(
                    media.file_url
                )

            elif media.media_type == "image":

                send_photo(
                    media.file_url
                )

        return {
            "message": "Published to Telegram"
        }