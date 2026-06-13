import requests


def publish_post(
    access_token: str,
    text: str
):

    url = "https://api.linkedin.com/rest/posts"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "LinkedIn-Version": "202401",
        "X-Restli-Protocol-Version": "2.0.0",
        "Content-Type": "application/json"
    }

    payload = {
        "commentary": text,
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