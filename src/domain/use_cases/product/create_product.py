from abc import ABC, abstractmethod

from src.domain.entities.product import Product


class CreateProductUseCaseInterface(ABC):
    @abstractmethod
    def execute(
        self, product: Product, created_by_id: int, company_id: int
    ) -> Product | None:
        pass
