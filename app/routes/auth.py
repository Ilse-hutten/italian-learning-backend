import pandas as pd
import datetime
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.utils.auth import (
    get_current_user,
    create_access_token,
    verify_password,
    get_password_hash,
)

router = APIRouter()

@router.post("/register")
async def register_user(username: str, email: str, password: str, db: Session = Depends(get_db)):
    # Check if user exists
    db_user = db.query(User).filter(User.email == email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = get_password_hash(password)
    new_user = User(
        email=email,
        username=username,
        hashed_password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created successfully"}

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    access_token = create_access_token(data={"sub": user.email})

    # Update last login
    user.last_login = datetime.datetime.utcnow()
    db.commit()

    return {"access_token": access_token, "token_type": "bearer"}
