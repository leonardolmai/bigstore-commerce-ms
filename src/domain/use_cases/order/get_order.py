from abc import ABC, abstractmethod

from src.domain.entities.order import Order


class GetOrderUseCaseInterface(ABC):
    @abstractmethod
    def execute(self, id: int) -> Order | None:
        pass
