from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..models.song import Song
from ..schemas.song import SongOut, SongLyrics

router = APIRouter()

@router.get("/", response_model=List[SongOut])
def get_songs(limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Song).order_by(Song.popularity.desc()).limit(limit).all()

@router.get("/{song_id}/lyrics", response_model=SongLyrics)
def get_song_lyrics(song_id: int, db: Session = Depends(get_db)):
    song = db.query(Song).filter(Song.id == song_id).first()
    if not song:
        raise HTTPException(status_code=404, detail="Song not found")

    return {
        "original": song.lyrics,
        "translation": song.translation,
        "vocabulary": song.vocabulary or {}
    }
