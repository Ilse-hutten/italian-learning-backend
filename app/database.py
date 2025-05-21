from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./italian_learning.db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# At the bottom of database.py
from app.models.user import User
from app.models.lesson import Lesson, LessonCategory
from app.models.song import Song
from app.models.progress import UserProgress

Base.metadata.create_all(bind=engine)
