from sqlalchemy import Column, Integer, String, Text, JSON  # Add JSON import
from ..database import Base
from sqlalchemy.orm import relationship

class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    artist = Column(String)
    year = Column(Integer, nullable=True)
    lyrics = Column(Text)                # Original Italian lyrics
    translation = Column(Text)           # English translation
    audio_file = Column(String)          # URL/path to audio file
    difficulty = Column(Integer)         # 1-5 difficulty rating
    popularity = Column(Integer)         # For sorting popular songs
    vocabulary = Column(JSON, nullable=True)  # Key phrases from the song

    # Relationship to progress tracking
    progress_entries = relationship("UserProgress", back_populates="song")
