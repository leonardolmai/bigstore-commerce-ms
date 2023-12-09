from abc import ABC, abstractmethod

from src.domain.entities.product import Product
from src.domain.entities.product_image import ProductImage


class ProductImageRepositoryInterface(ABC):
    @abstractmethod
    def list_product_images(self, product: Product) -> list[ProductImage] | None:
        pass

    @abstractmethod
    def get_product_image(self, id: int) -> ProductImage | None:
        pass

    @abstractmethod
    def create_product_image(self, product_image: ProductImage) -> ProductImage | None:
        pass

    def delete_product_image(self, id: int, product_id: int) -> bool:
        pass
