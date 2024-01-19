from abc import ABC, abstractmethod

from src.domain.entities.product_image import ProductImage


class DeleteProductImageUseCaseInterface(ABC):
    @abstractmethod
    def execute(self, id: int, product_id: int) -> ProductImage | None:
        pass
