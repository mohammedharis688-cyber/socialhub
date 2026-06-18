from sqlalchemy.orm import Session
import requests

from app.database import SessionLocal
from app.models import SocialAccount


class LinkedInProvider:

    def publish(self, post):

        db: Session = SessionLocal()

        try:

            account = (
                db.query(SocialAccount)
                .filter(
                    SocialAccount.user_id == post.user_id,
                    SocialAccount.platform == "linkedin"
                )
                .first()
            )

            if not account:
                return {
                    "error": "LinkedIn not connected"
                }

            url = "https://api.linkedin.com/rest/posts"

            headers = {
                "Authorization": f"Bearer {account.access_token}",
                "LinkedIn-Version": "202506",
                "X-Restli-Protocol-Version": "2.0.0",
                "Content-Type": "application/json"
            }

            payload = {
                "commentary": post.content,
                "author": f"urn:li:person:{account.platform_user_id}",
                "visibility": "PUBLIC",
                "distribution": {
                    "feedDistribution": "MAIN_FEED",
                    "targetEntities": [],
                    "thirdPartyDistributionChannels": []
                },
                "lifecycleState": "PUBLISHED",
                "isReshareDisabledByAuthor": False
            }

            response = requests.post(
                url,
                headers=headers,
                json=payload
            )

            return {
                "status_code": response.status_code,
                "response": response.text
            }

        finally:
            db.close()