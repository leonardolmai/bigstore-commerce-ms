from abc import ABC, abstractmethod

from src.domain.entities.product import Product


class ListProductsUseCaseInterface(ABC):
    @abstractmethod
    def execute(self) -> list[Product] | None:
        pass
