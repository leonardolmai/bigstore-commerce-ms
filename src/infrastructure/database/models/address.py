from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, backref, mapped_column, relationship

from src.infrastructure.database.models.base import Base


class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column("id", primary_key=True, unique=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    postal_code: Mapped[str] = mapped_column(String(length=8))
    uf: Mapped[str] = mapped_column(String(length=2))
    city: Mapped[str] = mapped_column(String(length=150))
    neighborhood: Mapped[str] = mapped_column(String(length=150))
    street: Mapped[str] = mapped_column(String(length=150))
    number: Mapped[str] = mapped_column(String(length=20))
    complement: Mapped[str] = mapped_column(String(length=150))
    user = relationship(
        "User",
        backref=backref("addresses", uselist=True),
        foreign_keys=[user_id],
    )
