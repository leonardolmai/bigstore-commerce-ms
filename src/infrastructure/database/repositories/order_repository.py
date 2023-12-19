from typing import Any

from sqlalchemy.orm import Session

from src.data.repositories.order_repository import OrderRepositoryInterface
from src.domain.entities.order import Order
from src.infrastructure.database.models.order import Order as OrderModel


class OrderRepository(OrderRepositoryInterface):
    def __init__(self, session: Session):
        self.session: Session = session

    def list_orders(self) -> list[Order] | None:
        try:
            orders = self.session.query(OrderModel).all()
            order_objects = []

            if orders:
                for order_model in orders:
                    order_data = {
                        "id": order_model.id,
                        "user_id": order_model.user_id,
                        "company_id": order_model.company_id,
                        "status": order_model.status.value,
                        "created_at": order_model.created_at,
                        "payment_method": order_model.payment_method.value,
                        "payment_details": order_model.payment_details,
                        "delivery_address": order_model.delivery_address,
                        "total": order_model.total,
                    }
                    order_object = Order(**order_data)
                    order_objects.append(order_object)

                return order_objects
            return orders
        except:
            return None

    def get_order(self, id: int) -> Order | None:
        try:
            order_model = (
                self.session.query(OrderModel).filter(OrderModel.id == id).one_or_none()
            )

            if order_model:
                order_data = {
                    "id": order_model.id,
                    "user_id": order_model.user_id,
                    "company_id": order_model.company_id,
                    "status": order_model.status.value,
                    "created_at": order_model.created_at,
                    "payment_method": order_model.payment_method.value,
                    "payment_details": order_model.payment_details,
                    "delivery_address": order_model.delivery_address,
                    "total": order_model.total,
                }
                order_object = Order(**order_data)
                return order_object
            return order_model
        except:
            return None

    def create_order(self, order: Order, user_id: int, company_id: int) -> Order | None:
        try:
            order_data = {
                "user_id": user_id,
                "company_id": company_id,
                # "status": order.status,
                "payment_method": order.payment_method,
                "payment_details": order.payment_details,
                "delivery_address": order.delivery_address,
                "total": order.total,
            }

            order_model = OrderModel(**order_data)

            self.session.add(order_model)
            self.session.commit()

            if order_model:
                order_data = {
                    "id": order_model.id,
                    "user_id": order_model.user_id,
                    "company_id": order_model.company_id,
                    "status": order_model.status.value,
                    "created_at": order_model.created_at,
                    "payment_method": order_model.payment_method.value,
                    "payment_details": order_model.payment_details,
                    "delivery_address": order_model.delivery_address,
                    "total": order_model.total,
                }
                order_object = Order(**order_data)
                return order_object

            return order_model
        except:
            return None

    def update_order(self, id: int, update_fields: dict[str, Any]) -> Order | None:
        try:
            self.session.query(OrderModel).filter(OrderModel.id == id).update(
                update_fields
            )
            self.session.commit()
            order_updated = self.get_order(id)

            return order_updated
        except:
            return None
