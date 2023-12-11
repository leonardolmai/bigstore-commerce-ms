from typing import Any

from src.data.repositories.product_repository import ProductRepositoryInterface
from src.domain.entities.product import Product
from src.domain.use_cases.product.update_product import UpdateProductUseCaseInterface


class UpdateProductUseCase(UpdateProductUseCaseInterface):
    def __init__(self, product_repository: ProductRepositoryInterface) -> None:
        self.__product_repository = product_repository

    def execute(self, id, update_fields: dict[str, Any]) -> Product | None:
        product = self.__product_repository.update_product(id, update_fields)
        return product
