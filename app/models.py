from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)
from app.database import Base
from sqlalchemy import Table
from sqlalchemy.orm import relationship

post_media = Table(
    "post_media",
    Base.metadata,

    Column(
        "post_id",
        Integer,
        ForeignKey("posts.id")
    ),

    Column(
        "media_id",
        Integer,
        ForeignKey("media.id")
    )
)
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String, unique=True, nullable=False)

    password_hash = Column(String, nullable=False)

class SocialAccount(Base):
    __tablename__ = "social_accounts"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    platform = Column(
        String,
        nullable=False
    )

    access_token = Column(
        String(2000),
        nullable=False
    )

    refresh_token = Column(
        String(2000),
        nullable=True
    )

    platform_user_id = Column(
        String(255),
        nullable=True
    )

    platform_username = Column(
        String(255),
        nullable=True
    )

class Post(Base):
    __tablename__ = "posts"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    content = Column(
        String,
        nullable=False
    )

    status = Column(
        String,
        default="draft"
    )

    scheduled_at = Column(
        String,
        nullable=True
    )
    media = relationship(
        "Media",
        secondary=post_media,
        back_populates="posts"
    )

class Media(Base):
    __tablename__ = "media"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    post_id = Column(
        Integer,
        ForeignKey("posts.id")
    )

    file_name = Column(
        String,
        nullable=False
    )

    file_url = Column(
        String,
        nullable=False
    )

    media_type = Column(
        String,
        nullable=False
    )
    posts = relationship(
        "Post",
        secondary=post_media,
        back_populates="media"
    )


