from abc import ABC, abstractmethod

from src.domain.entities.order import Order


class CreateOrderUseCaseInterface(ABC):
    @abstractmethod
    def execute(self, order: Order, user_id: int, company_id: int) -> Order | None:
        pass
