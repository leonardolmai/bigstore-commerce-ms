from sqlalchemy import Float, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, backref, mapped_column, relationship

from src.infrastructure.database.models.base import Base


class OrderItem(Base):
    __tablename__ = "order_item"

    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("order.id"), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"), nullable=False)
    name: Mapped[str] = mapped_column(String(255))
    price: Mapped[float] = mapped_column(Float)
    quantity: Mapped[int] = mapped_column(Integer)

    order = relationship(
        "Order", backref=backref("order_items", lazy="dynamic"), foreign_keys=[order_id]
    )
    product = relationship(
        "Product",
        backref=backref("order_items", lazy="dynamic"),
        foreign_keys=[product_id],
    )

    __table_args__ = (
        UniqueConstraint("order_id", "product_id", name="unique_order_product"),
    )
