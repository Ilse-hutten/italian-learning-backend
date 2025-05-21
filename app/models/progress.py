from sqlalchemy import Column, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship  # <-- Add this import
from datetime import datetime
from app.database import Base

class UserProgress(Base):
    __tablename__ = "user_progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    lesson_id = Column(Integer, ForeignKey("lessons.id"), nullable=True)
    song_id = Column(Integer, ForeignKey("songs.id"), nullable=True)
    completed = Column(Boolean, default=False)
    score = Column(Integer)                # Percentage score
    last_attempted = Column(DateTime, default=datetime.utcnow)
    times_attempted = Column(Integer, default=1)
    xp_earned = Column(Integer, default=0) # XP points from this activity

    # Add these relationships
    song = relationship("Song", back_populates="progress_entries")
    lesson = relationship("Lesson", back_populates="progress_entries")
    user = relationship("User", back_populates="progress")
