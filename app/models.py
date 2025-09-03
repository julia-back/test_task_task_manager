from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Text
import uuid


Base = declarative_base()


class Task(Base):

    __tablename__ = "tasks"

    STATUS_CHOICES = [
        ("created", "Создано"),
        ("processed", "В работе"),
        ("closed", "Завершено"),
    ]

    uuid = Column(String(36), primary_key=True, default=lambda: uuid.uuid4())
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    status = Column(String(), choices=STATUS_CHOICES)
