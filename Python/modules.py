from datetime import datetime
from typing import List
from sqlalchemy import Column, ForeignKey, DateTime, UUID, String
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from config import db, Base
import uuid



class User(Base):
    __tablename__ = "Users"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username: Mapped[str] = mapped_column(unique=True)
    items: Mapped[List["Item"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __init__(self, username: str):
        self.username = username

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r}, items={len(self.items)!r})"


class Item(Base):
    __tablename__ = "Items"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("Users.id"))
    item_name: Mapped[str] = mapped_column(String(120), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(200))
    barcode: Mapped[str] = mapped_column(String(120), nullable=False)
    item_link: Mapped[str] = mapped_column(String(200))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    user: Mapped["User"] = relationship(back_populates="items")

    def __init__(self, item_name: str, description: Optional[str], barcode: str, item_link: str):
        self.item_name = item_name
        self.description = description
        self.barcode = barcode
        self.item_link = item_link
        self.created_at = datetime.now()

    def __repr__(self) -> str:
        return f"Item(id={self.id!r}, item_name={self.item_name!r}, description={self.description!r}, barcode={self.barcode!r}, created_at={self.created_at!r}, user_id={self.user_id!r})"
