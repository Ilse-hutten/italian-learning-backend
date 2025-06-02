# Correct import statement
from ..models.progress import UserProgress  # Explicit import
from ..models.lesson import Lesson
from ..models.song import Song
from sqlalchemy.orm import Session
from sqlalchemy import or_
import random
import datetime
from datetime import datetime, timedelta



def generate_xp(score: float, time_spent: int) -> int:
    """Calculate XP based on performance metrics"""
    base_xp = 10
    score_bonus = int(score * 20)  # 0-20 points
    time_bonus = min(time_spent // 30, 10)  # 1 point per 30s, max 10
    return base_xp + score_bonus + time_bonus

def check_streak(last_login: datetime) -> int:
    """Determine if user maintained their daily streak"""
    if not last_login:
        return 0
    return 1 if datetime.utcnow() - last_login < timedelta(hours=36) else 0

def select_review_items(user_id: int, db: Session) -> list:
    """Select lessons/songs for spaced repetition review"""
    # Get user's progress records that need review
    progress_records = (
        db.query(UserProgress)
        .filter(
            UserProgress.user_id == user_id,
            UserProgress.score < 70,  # Using the actual column from UserProgress
            or_(
                UserProgress.lesson_id.is_not(None),
                UserProgress.song_id.is_not(None)
            )
        )
        .order_by(UserProgress.score.asc())  # Worst scores first
        .limit(50)
        .all()
    )

    # Extract the actual lesson/song objects
    review_items = []
    for record in progress_records:
        if record.lesson_id:
            review_items.append(record.lesson)
        elif record.song_id:
            review_items.append(record.song)

    # Fallback to new items if no reviews needed
    if not review_items:
        new_lessons = db.query(Lesson).limit(25).all()
        new_songs = db.query(Song).limit(25).all()
        review_items = new_lessons + new_songs

    return random.sample(review_items, min(5, len(review_items)))

def sanitize_input(text: str) -> str:
    """Basic input sanitization"""
    return text.strip().replace("<", "&lt;").replace(">", "&gt;")

def format_lyrics(lyrics: str) -> list:
    """Convert raw lyrics into timed sections for karaoke-style display"""
    return [{"text": line, "time": i*2} for i, line in enumerate(lyrics.split("\n")) if line]
