from abc import ABC, abstractmethod

from src.domain.entities.product_image import ProductImage


class CreateProductImageUseCaseInterface(ABC):
    @abstractmethod
    def execute(self, product_image: ProductImage) -> ProductImage | None:
        pass
