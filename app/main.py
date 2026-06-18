from fastapi import FastAPI

from app.database import engine, Base
from app.routers.social_accounts import (
    router as social_router
)
from app.models import (
    User,
    SocialAccount,
    Post,
    Media
)
# from app.routers.linkedin import (
#     router as linkedin_router
# )
from app.routers.users import router as user_router
from app.routers.posts import router as post_router
app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(post_router)
app.include_router(social_router)
# app.include_router(linkedin_router)

@app.get("/")
def home():
    return {"message": "SocialHub API Running"}