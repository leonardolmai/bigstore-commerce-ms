from abc import ABC, abstractmethod
from typing import Any

from src.domain.entities.product import Product


class ProductRepositoryInterface(ABC):
    @abstractmethod
    def list_products(self) -> list[Product] | None:
        pass

    @abstractmethod
    def get_product(self, id: int) -> Product | None:
        pass

    @abstractmethod
    def create_product(
        self, product: Product, created_by_id: int, company_id: int
    ) -> Product | None:
        pass

    @abstractmethod
    def update_product(self, id: int, update_fields: dict[str, Any]) -> Product | None:
        pass

    @abstractmethod
    def delete_product(self, id: int) -> bool:
        pass
