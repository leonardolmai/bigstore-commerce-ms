from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, backref, mapped_column, relationship

from src.infrastructure.database.models.base import Base


class ProductImage(Base):
    __tablename__ = "product_image"

    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"), nullable=False)
    image: Mapped[str] = mapped_column(String(255))

    product = relationship(
        "Product",
        backref=backref("images", lazy="dynamic"),
        foreign_keys=[product_id],
    )
