from sqlalchemy import Column, Integer, String, Boolean, DateTime
from ..database import Base
import datetime
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    last_login = Column(DateTime)
    streak_days = Column(Integer, default=0)
    xp_points = Column(Integer, default=0)
    progress = relationship("UserProgress", back_populates="user")

    # Relationships would be defined here (e.g., progress records)
