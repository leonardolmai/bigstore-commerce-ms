from sqlalchemy.orm import Session

from src.data.repositories.order_item_repository import OrderItemRepositoryInterface
from src.domain.entities.order import Order
from src.domain.entities.order_item import OrderItem
from src.infrastructure.database.models.order_item import OrderItem as OrderItemModel


class OrderItemRepository(OrderItemRepositoryInterface):
    def __init__(self, session: Session):
        self.session: Session = session

    def list_order_items(self, order: Order) -> list[OrderItem] | None:
        try:
            return self.session.query(OrderItemModel).filter_by(order_id=order.id).all()
        except:
            return None

    def get_order_item(self, id: int) -> OrderItem | None:
        try:
            return (
                self.session.query(OrderItemModel)
                .filter(OrderItemModel.id == id)
                .one_or_none()
            )
        except:
            return None

    def create_order_item(self, order_item: OrderItem) -> OrderItem | None:
        try:
            order_item_data = {
                "product_id": order_item.product_id,
                "order_id": order_item.order_id,
                "name": order_item.name,
                "price": order_item.price,
                "quantity": order_item.quantity,
            }
            order_item_model = OrderItemModel(**order_item_data)

            self.session.add(order_item_model)
            self.session.commit()
            self.session.refresh(order_item_model)
            return order_item_model
        except:
            return None
