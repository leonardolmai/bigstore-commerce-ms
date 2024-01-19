from abc import ABC, abstractmethod

from src.domain.entities.order_item import OrderItem


class CreateOrderItemUseCaseInterface(ABC):
    @abstractmethod
    def execute(self, order_item: OrderItem) -> OrderItem | None:
        pass
