from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, backref, mapped_column, relationship

from src.infrastructure.database.models.base import Base


class Card(Base):
    __tablename__ = "card"

    id: Mapped[int] = mapped_column("id", primary_key=True, unique=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    name: Mapped[str] = mapped_column(String(length=255))
    number: Mapped[str] = mapped_column(String(length=16))
    expiration_month: Mapped[str] = mapped_column(String(length=2))
    expiration_year: Mapped[str] = mapped_column(String(length=4))
    cvc: Mapped[str] = mapped_column(String(length=3))
    user = relationship(
        "User",
        backref=backref("cards", uselist=True),
        foreign_keys=[user_id],
    )
