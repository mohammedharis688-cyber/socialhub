import requests


def publish_post(
    access_token: str,
    platform_user_id: str,
    text: str
):
    url = "https://api.linkedin.com/rest/posts"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "LinkedIn-Version": "202506",
        "X-Restli-Protocol-Version": "2.0.0",
        "Content-Type": "application/json"
    }

    payload = {
        "commentary": text,
        "author": f"urn:li:person:{platform_user_id}",
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