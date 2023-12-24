from abc import ABC, abstractmethod

from src.domain.entities.order_item import OrderItem


class GetOrderItemUseCaseInterface(ABC):
    @abstractmethod
    def execute(self, id: int) -> OrderItem | None:
        pass
