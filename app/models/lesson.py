from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class LessonCategory(Base):
    __tablename__ = "lesson_categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    icon = Column(String)
    description = Column(String)

    # Relationship
    lessons = relationship("Lesson", back_populates="category")

class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    category_id = Column(Integer, ForeignKey("lesson_categories.id"))
    content = Column(JSON)  # Stores all lesson data
    difficulty = Column(Integer, default=1)
    order = Column(Integer)

    # Relationships
    category = relationship("LessonCategory", back_populates="lessons")
    progress_entries = relationship("UserProgress", back_populates="lesson")
