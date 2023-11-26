from sqlalchemy import Enum, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, backref, mapped_column, relationship

from src.infrastructure.database.models.base import Base
from src.infrastructure.database.models.enums.product_category import ProductCategory


class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    price: Mapped[float] = mapped_column(Float)
    quantity: Mapped[int] = mapped_column(Integer)
    description: Mapped[str | None] = mapped_column(Text)
    is_approved: Mapped[bool] = mapped_column(default=False)
    created_by_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    company_id: Mapped[int] = mapped_column(ForeignKey("company.id"), nullable=False)
    category: Mapped[ProductCategory] = mapped_column(
        Enum(ProductCategory), nullable=False
    )

    created_by = relationship(
        "User",
        backref=backref("products", lazy="dynamic"),
        foreign_keys=[created_by_id],
    )
    company = relationship(
        "Company",
        backref=backref("products", lazy="dynamic"),
        foreign_keys=[company_id],
    )
