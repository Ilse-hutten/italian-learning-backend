from pydantic import BaseModel
from typing import Dict, List, Optional
from datetime import datetime

class SongBase(BaseModel):
    title: str
    artist: str
    difficulty: int

class SongCreate(SongBase):
    lyrics: str
    translation: str
    audio_file: str
    vocabulary: Optional[Dict] = None  # For key phrases
    year: Optional[int] = None

class SongOut(SongBase):
    id: int
    popularity: int
    vocabulary: Optional[Dict] = None

    class Config:
        orm_mode = True

class SongLyrics(BaseModel):
    original: str
    translation: str
    vocabulary: Dict[str, str]  # {"Italian phrase": "English translation"}
