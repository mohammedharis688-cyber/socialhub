from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.auth import get_current_user
from app.models import SocialAccount


router = APIRouter(
    prefix="/social",
    tags=["Social Accounts"]
)


@router.post("/connect/{platform}")
def connect_platform(
    platform: str,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    existing = (
        db.query(SocialAccount)
        .filter(
            SocialAccount.user_id == current_user.id,
            SocialAccount.platform == platform
        )
        .first()
    )

    if existing:
        return {
            "message": f"{platform} already connected"
        }

    account = SocialAccount(
        user_id=current_user.id,
        platform=platform,
        access_token="connected",
        refresh_token=None
    )

    db.add(account)
    db.commit()

    return {
        "message": f"{platform} connected"
    }


@router.get("/accounts")
def get_connected_accounts(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    accounts = (
        db.query(SocialAccount)
        .filter(
            SocialAccount.user_id == current_user.id
        )
        .all()
    )

    return accounts