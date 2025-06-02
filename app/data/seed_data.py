import sys
import os

# Add the project root (italian-learning-backend) to Python path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

# Now your imports will work
import json
from sqlalchemy.orm import Session
from app.database import engine, Base, SessionLocal
from app.models import LessonCategory, Lesson, Song

import json
from sqlalchemy.orm import Session
#from database import engine, Base
#from models import LessonCategory, Lesson, Song

def seed_data(db: Session):
    # Seed Themes/Categories - Check for existence first
    themes = [
        {"name": "Restaurant", "icon": "🍝", "description": "Ordering food and drinks"},
        {"name": "Transportation", "icon": "🚆", "description": "Getting around Italy"},
        {"name": "Shopping", "icon": "🛍️", "description": "Stores and markets"},
        {"name": "Emergency", "icon": "🚨", "description": "Essential emergency phrases"}
    ]

    for theme in themes:
        # Check if category already exists
        existing = db.query(LessonCategory).filter_by(name=theme["name"]).first()
        if not existing:
            db.add(LessonCategory(**theme))
            print(f"Added category: {theme['name']}")
        else:
            print(f"Category already exists: {theme['name']}")
    db.commit()

    # Seed Lessons - Check for existence first
    restaurant_phrases = [
        {"italian": "Un tavolo per due", "english": "A table for two", "pronunciation": "oon TAH-volo per DUE"},
        {"italian": "Il conto, per favore", "english": "The bill, please", "pronunciation": "eel KON-to per fa-VO-re"}
    ]

    lessons = [
        {
            "title": "Restaurant Basics",
            "category_id": 1,
            "content": {
                "phrases": restaurant_phrases,
                "exercises": [
                    {
                        "type": "flashcard",
                        "question": "How do you ask for the bill?",
                        "answer": "Il conto, per favore"
                    }
                ]
            },
            "difficulty": 1
        }
    ]

    for lesson in lessons:
        # Check if lesson already exists
        existing = db.query(Lesson).filter_by(title=lesson["title"]).first()
        if not existing:
            db.add(Lesson(**lesson))
            print(f"Added lesson: {lesson['title']}")
        else:
            print(f"Lesson already exists: {lesson['title']}")
    db.commit()

    # Seed Songs - Check for existence first
    songs = [
        {
            "title": "Volare",
            "artist": "Domenico Modugno",
            "year": 1958,
            "lyrics": "Nel blu dipinto di blu\nFelice di stare lassù",
            "translation": "In the blue painted blue\nHappy to stay up there",
            "audio_file": "songs/volare.mp3",
            "difficulty": 2,
            "popularity": 100,
            "vocabulary": {
                "phrases": [
                    {
                        "italian": "Volare",
                        "english": "To fly",
                        "example": "Nel blu dipinto di blu"
                    }
                ]
            }
        }
    ]

    for song in songs:
        # Check if song already exists
        existing = db.query(Song).filter_by(title=song["title"], artist=song["artist"]).first()
        if not existing:
            db.add(Song(**song))
            print(f"Added song: {song['title']} by {song['artist']}")
        else:
            print(f"Song already exists: {song['title']} by {song['artist']}")
    db.commit()

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        seed_data(db)
        print("Database seeded successfully!")
    finally:
        db.close()
