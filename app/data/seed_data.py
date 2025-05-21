import json
from sqlalchemy.orm import Session
from app.database import engine, Base
from app.models import LessonCategory, Lesson, Song

def seed_data(db: Session):
    # Seed Themes/Categories
    themes = [
        {"name": "Restaurant", "icon": "🍝", "description": "Ordering food and drinks"},
        {"name": "Transportation", "icon": "🚆", "description": "Getting around Italy"},
        {"name": "Shopping", "icon": "🛍️", "description": "Stores and markets"},
        {"name": "Emergency", "icon": "🚨", "description": "Essential emergency phrases"}
    ]

    for theme in themes:
        db.add(LessonCategory(**theme))
    db.commit()

    # Seed Lessons
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
        db.add(Lesson(**lesson))
    db.commit()

    # Seed Songs
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
        db.add(Song(**song))
    db.commit()

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    from app.database import SessionLocal
    db = SessionLocal()
    seed_data(db)
    print("Database seeded successfully!")
