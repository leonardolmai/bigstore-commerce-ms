from abc import ABC, abstractmethod

from src.domain.entities.product_image import ProductImage


class ListProductImagesUseCaseInterface(ABC):
    @abstractmethod
    def execute(self, product) -> list[ProductImage] | None:
        pass
