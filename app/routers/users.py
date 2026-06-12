from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.auth import get_current_user
from app.schemas import UserRegister
from app.database import get_db
from app.auth import hash_password
from app.models import User
from app.schemas import UserLogin
from app.auth import (
    verify_password,
    create_access_token
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):

    existing_user = (
        db.query(User)
        .filter(User.email == user.email)
        .first()
    )

    if existing_user:
        return {"error": "Email already exists"}

    new_user = User(
        email=user.email,
        password_hash=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()

    return {"message": "User Registered"}

@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    db_user = (
        db.query(User)
        .filter(User.email == user.email)
        .first()
    )

    if not db_user:
        return {"error": "Invalid credentials"}

    if not verify_password(
        user.password,
        db_user.password_hash
    ):
        return {"error": "Invalid credentials"}

    access_token = create_access_token(
        {
            "sub": db_user.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@router.get("/me")
def get_me(
    current_user = Depends(get_current_user)
):

    return {
        "id": current_user.id,
        "email": current_user.email
    }



