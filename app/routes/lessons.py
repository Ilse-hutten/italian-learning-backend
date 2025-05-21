from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.lesson import Lesson, LessonCategory
from app.schemas.lesson import LessonOut, LessonCategoryOut, LessonContent

router = APIRouter()

@router.get("/categories", response_model=List[LessonCategoryOut])
def get_categories(db: Session = Depends(get_db)):
    return db.query(LessonCategory).all()

@router.get("/{lesson_id}", response_model=LessonOut)
def get_lesson(lesson_id: int, db: Session = Depends(get_db)):
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return lesson

@router.get("/{lesson_id}/content", response_model=LessonContent)
def get_lesson_content(lesson_id: int, db: Session = Depends(get_db)):
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return lesson.content  # Returns the JSON content directly
