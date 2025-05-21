from app.database import SessionLocal
from app.models import LessonCategory, Lesson, Song

db = SessionLocal()

print("\n=== Categories ===")
for category in db.query(LessonCategory).all():
    print(f"{category.id}: {category.name} ({category.icon})")

print("\n=== Lessons ===")
for lesson in db.query(Lesson).all():
    print(f"{lesson.id}: {lesson.title} (Category: {lesson.category_id})")
    print(f"Phrases: {lesson.content['phrases']}")

print("\n=== Songs ===")
for song in db.query(Song).all():
    print(f"{song.id}: {song.title} by {song.artist}")
    print(f"First line: {song.lyrics.split('\n')[0]}")

db.close()
