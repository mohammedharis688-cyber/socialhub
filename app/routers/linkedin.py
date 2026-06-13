from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from app.services.linkedin_service import (
    get_authorization_url,
    get_access_token
)
from fastapi import Request
router = APIRouter(
    prefix="/social/linkedin",
    tags=["LinkedIn"]
)
from app.models import SocialAccount
from app.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from app.services.linkedin_service import (
    get_profile
)
from app.providers.linkedin import publish_post


@router.get("/login")
def linkedin_login():

    url = get_authorization_url()

    return RedirectResponse(url)




@router.get("/callback")
def linkedin_callback(
    request: Request,
    code: str = None,
    error: str = None,
    error_description: str = None
):

    if error:
        return {
            "error": error,
            "description": error_description
        }

    token_data = get_access_token(code)

    return token_data

@router.get("/profile")
def linkedin_profile(
    db: Session = Depends(get_db)
):

    account = (
        db.query(SocialAccount)
        .filter(
            SocialAccount.user_id == 2,
            SocialAccount.platform == "linkedin"
        )
        .first()
    )

    return get_profile(
        account.access_token
    )

@router.post("/test-post")
def linkedin_test_post(
    db: Session = Depends(get_db)
):

    account = (
        db.query(SocialAccount)
        .filter(
            SocialAccount.user_id == 2,
            SocialAccount.platform == "linkedin"
        )
        .first()
    )

    return publish_post(
        account.access_token,
        """🚀 SocialHub Integration Test
This post was published automatically through my SocialHub FastAPI project.
#Testing #API #LinkedIn"""
    )