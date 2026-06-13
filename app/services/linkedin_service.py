import requests
from jose import jwt
from app.config import (
    LINKEDIN_CLIENT_ID,
    LINKEDIN_CLIENT_SECRET
)

REDIRECT_URI = (
    "http://localhost:8000/social/linkedin/callback"
)


def get_authorization_url():

    scope = "openid profile email w_member_social"

    return (
        "https://www.linkedin.com/oauth/v2/authorization"
        f"?response_type=code"
        f"&client_id={LINKEDIN_CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        f"&scope={scope}"
    )


def get_access_token(code: str):

    url = (
        "https://www.linkedin.com/oauth/v2/accessToken"
    )

    data = {
        "grant_type": "authorization_code",
        "code": code,
        "client_id": LINKEDIN_CLIENT_ID,
        "client_secret": LINKEDIN_CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI
    }

    response = requests.post(
        url,
        data=data
    )

    return response.json()

def get_profile(access_token: str):

    url = "https://api.linkedin.com/v2/userinfo"

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(
        url,
        headers=headers
    )

    return response.json()

def get_userinfo(access_token: str):

    url = "https://api.linkedin.com/v2/userinfo"

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(
        url,
        headers=headers
    )

    return {
        "status_code": response.status_code,
        "response": response.json()
    }


def decode_id_token(id_token: str):

    return jwt.get_unverified_claims(
        id_token
    )