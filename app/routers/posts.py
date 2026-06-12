from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import UploadFile, File
from app.database import get_db
from app.auth import get_current_user
from app.models import Post
from app.schemas import PostCreate
from app.models import Media
from app.services.telegram_service import (
    send_message,
    send_document,
    send_photo
)
from app.providers.provider_registry import (
    get_provider
)
from app.models import SocialAccount
import uuid
import shutil
import os
router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.post("/")
def create_post(
    post: PostCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    new_post = Post(
        user_id=current_user.id,
        content=post.content,
        status="draft"
    )

    for media_id in post.media_ids:

        media = (
            db.query(Media)
            .filter(Media.id == media_id)
            .first()
        )

        if media:
            new_post.media.append(media)

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return {
        "message": "Post created",
        "post_id": new_post.id
    }
@router.get("/")
def get_posts(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    posts = (
        db.query(Post)
        .filter(Post.user_id == current_user.id)
        .all()
    )

    return posts

@router.post("/upload")
def upload_file(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    upload_dir = "uploads"

    os.makedirs(
        upload_dir,
        exist_ok=True
    )

    unique_filename = (
        f"{uuid.uuid4()}_{file.filename}"
    )

    file_path = os.path.join(
        upload_dir,
        unique_filename
    )
    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    if file.content_type.startswith("image"):
        media_type = "image"

    elif file.content_type == "application/pdf":
        media_type = "document"

    else:
        media_type = "other"


    media = Media(
        file_name=file.filename,
        file_url=file_path,
        media_type=media_type
    )

    db.add(media)
    db.commit()
    db.refresh(media)

    return {
        "media_id": media.id,
        "file_name": media.file_name,
        "media_type": media.media_type,
        "file_url": media.file_url
    }
@router.post("/{post_id}/publish-all")
def publish_all(
    post_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    post = (
        db.query(Post)
        .filter(
            Post.id == post_id,
            Post.user_id == current_user.id
        )
        .first()
    )

    if not post:
        return {
            "error": "Post not found"
        }

    accounts = (
        db.query(SocialAccount)
        .filter(
            SocialAccount.user_id == current_user.id
        )
        .all()
    )

    published_to = []

    for account in accounts:

        provider = get_provider(
            account.platform
        )

        if provider:

            provider.publish(post)

            published_to.append(
                account.platform
            )

    return {
        "message": "Published successfully",
        "platforms": published_to
    }
@router.post("/{post_id}/publish/{platform}")
def publish_post(
    post_id: int,
    platform: str,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    post = (
        db.query(Post)
        .filter(
            Post.id == post_id,
            Post.user_id == current_user.id
        )
        .first()
    )

    if not post:
        return {
            "error": "Post not found"
        }

    provider = get_provider(
        platform
    )

    if not provider:
        return {
            "error": "Platform not supported"
        }

    return provider.publish(post)

