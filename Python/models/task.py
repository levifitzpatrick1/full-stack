from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from config import db


class Task(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str]
    completed: Mapped[bool]

    def __init__(self, content):
        self.content = content
        self.completed = False
