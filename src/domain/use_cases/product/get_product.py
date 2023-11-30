from abc import ABC, abstractmethod

from src.domain.entities.product import Product


class GetProductUseCaseInterface(ABC):
    @abstractmethod
    def execute(self, id: int) -> Product | None:
        pass
