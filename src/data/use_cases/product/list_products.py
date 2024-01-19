from src.data.repositories.product_repository import ProductRepositoryInterface
from src.domain.entities.product import Product
from src.domain.use_cases.product.list_products import ListProductsUseCaseInterface


class ListProductsUseCase(ListProductsUseCaseInterface):
    def __init__(self, product_repository: ProductRepositoryInterface) -> None:
        self.__product_repository = product_repository

    def execute(self) -> list[Product] | None:
        products = self.__product_repository.list_products()
        return products
