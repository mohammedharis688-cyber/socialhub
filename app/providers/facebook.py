from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import SocialAccount

from app.services.facebook_service import (
    publish_post
)


class FacebookProvider:

    def publish(self, post):

        db: Session = SessionLocal()

        try:

            account = (
                db.query(SocialAccount)
                .filter(
                    SocialAccount.user_id == post.user_id,
                    SocialAccount.platform == "facebook"
                )
                .first()
            )

            if not account:

                return {
                    "error": "Facebook not connected"
                }

            return publish_post(
                account.platform_user_id,
                account.access_token,
                post.content
            )

        finally:
            db.close()