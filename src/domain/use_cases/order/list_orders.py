from abc import ABC, abstractmethod

from src.domain.entities.order import Order


class ListOrdersUseCaseInterface(ABC):
    @abstractmethod
    def execute(self) -> list[Order] | None:
        pass
