from datetime import datetime
from typing import List
from sqlalchemy import Column, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from config import db, Base


class User(Base):
    __tablename__ = "Users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str]
    tasks: Mapped[List["Task"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r}, email={self.email!r}, tasks={self.tasks!r})"


class Task(Base):
    __tablename__ = "Tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("Users.id"))
    title = Column(db.String(120), nullable=False)
    description = Column(db.String(200))
    completed: Mapped[bool]
    created_at = Column(DateTime, default=datetime.now)
    due_at = Column(DateTime, nullable=True)

    user: Mapped["User"] = relationship(back_populates="tasks")

    def __init__(self, title: str, description: str, due_at=None):
        self.title = title
        self.description = description
        self.completed = False
        self.created_at = datetime.now()
        self.due_at = due_at

    def __repr__(self) -> str:
        return f"Task(id={self.id!r}, title={self.title!r}, description={self.description!r}, completed={self.completed}, user={self.user_id!r})"
