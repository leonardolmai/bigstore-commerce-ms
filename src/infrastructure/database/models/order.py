from datetime import datetime

from sqlalchemy import DateTime, Enum, Float, ForeignKey, Text
from sqlalchemy.orm import Mapped, backref, mapped_column, relationship

from src.infrastructure.database.models.base import Base
from src.infrastructure.database.models.enums.order_status import OrderStatus
from src.infrastructure.database.models.enums.payment_method import PaymentMethod


class Order(Base):
    __tablename__ = "order"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    company_id: Mapped[int] = mapped_column(ForeignKey("company.id"), nullable=False)
    status: Mapped[OrderStatus] = mapped_column(
        Enum(OrderStatus), nullable=False, default=OrderStatus.PENDING
    )
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    payment_method: Mapped[PaymentMethod] = mapped_column(
        Enum(PaymentMethod), nullable=False
    )
    payment_details: Mapped[str] = mapped_column(Text)
    delivery_address: Mapped[str] = mapped_column(Text)
    total: Mapped[float] = mapped_column(Float(10, 2))

    user = relationship(
        "User",
        backref=backref("orders", lazy="dynamic"),
        foreign_keys=[user_id],
    )
    company = relationship(
        "Company",
        backref=backref("orders", lazy="dynamic"),
        foreign_keys=[company_id],
    )
