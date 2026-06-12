from fastapi import FastAPI

from app.database import engine, Base

from app.models import (
    User,
    SocialAccount,
    Post,
    Media
)
from app.routers.users import router as user_router
from app.routers.posts import router as post_router
app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(post_router)



@app.get("/")
def home():
    return {"message": "SocialHub API Running"}