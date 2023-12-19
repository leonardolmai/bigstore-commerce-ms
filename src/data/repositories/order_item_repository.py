from abc import ABC, abstractmethod

from src.domain.entities.order import Order
from src.domain.entities.order_item import OrderItem


class OrderItemRepositoryInterface(ABC):
    @abstractmethod
    def list_order_items(self, order: Order) -> list[OrderItem] | None:
        pass

    @abstractmethod
    def get_order_item(self, id: int) -> OrderItem | None:
        pass

    @abstractmethod
    def create_order_item(self, order_item: OrderItem) -> OrderItem | None:
        pass
