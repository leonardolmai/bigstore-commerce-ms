from abc import ABC, abstractmethod

from src.domain.entities.order_item import OrderItem


class ListOrderItemsUseCaseInterface(ABC):
    @abstractmethod
    def execute(self, order) -> list[OrderItem] | None:
        pass
