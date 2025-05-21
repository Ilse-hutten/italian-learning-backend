from pydantic import BaseModel
from typing import Optional, List, Dict
from datetime import datetime

class LessonBase(BaseModel):
    title: str
    category_id: int
    order: Optional[int] = 0

class LessonCreate(LessonBase):
    content: Dict  # Stores phrases, exercises, etc.

class LessonOut(LessonBase):
    id: int
    difficulty: int
    created_at: datetime

    class Config:
        orm_mode = True

class LessonCategoryOut(BaseModel):
    id: int
    name: str
    icon: str
    description: Optional[str]

    class Config:
        orm_mode = True

class LessonContent(BaseModel):
    phrases: List[Dict]  # [{"italian": "Ciao", "english": "Hello"}]
    exercises: List[Dict]
    audio_files: Optional[List[str]]
