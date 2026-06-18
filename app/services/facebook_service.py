import requests


def publish_post(
    page_id: str,
    access_token: str,
    content: str
):

    url = (
        f"https://graph.facebook.com/v25.0/"
        f"{page_id}/feed"
    )

    data = {
        "message": content,
        "access_token": access_token
    }

    response = requests.post(
        url,
        data=data,
        timeout=10
    )

    return {
        "status_code": response.status_code,
        "response": response.text
    }