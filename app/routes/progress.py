# Provides an API endpoint for your Flutter app to interact with progress data

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.progress import UserProgress
from app.database import get_db

router = APIRouter()

@router.post("/")
def create_progress(
    user_id: int,
    lesson_id: int = None,
    song_id: int = None,
    score: int = 0,
    db: Session = Depends(get_db)
):
    progress = UserProgress(
        user_id=user_id,
        lesson_id=lesson_id,
        song_id=song_id,
        score=score
    )
    db.add(progress)
    db.commit()
    return {"status": "success"}
