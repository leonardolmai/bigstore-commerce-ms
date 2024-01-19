from src.data.repositories.product_repository import ProductRepositoryInterface
from src.domain.entities.product import Product
from src.domain.use_cases.product.get_product import GetProductUseCaseInterface


class GetProductUseCase(GetProductUseCaseInterface):
    def __init__(self, product_repository: ProductRepositoryInterface) -> None:
        self.__product_repository = product_repository

    def execute(self, id: int) -> Product | None:
        product = self.__product_repository.get_product(id)
        return product
