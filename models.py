from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from datetime import datetime


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    course = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)