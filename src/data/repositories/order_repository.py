from abc import ABC, abstractmethod
from typing import Any

from src.domain.entities.order import Order


class OrderRepositoryInterface(ABC):
    @abstractmethod
    def list_orders(self) -> list[Order] | None:
        pass

    @abstractmethod
    def get_order(self, id: int) -> Order | None:
        pass

    @abstractmethod
    def create_order(self, order: Order, user_id: int, company_id: int) -> Order | None:
        pass

    @abstractmethod
    def update_order(self, id: int, update_fields: dict[str, Any]) -> Order | None:
        pass
