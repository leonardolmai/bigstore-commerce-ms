from src.data.repositories.product_repository import ProductRepositoryInterface
from src.domain.entities.product import Product
from src.domain.use_cases.product.create_product import CreateProductUseCaseInterface


class CreateProductUseCase(CreateProductUseCaseInterface):
    def __init__(self, product_repository: ProductRepositoryInterface) -> None:
        self.__product_repository = product_repository

    def execute(
        self, product: Product, created_by_id: int, company_id: int
    ) -> Product | None:
        product = self.__product_repository.create_product(
            product, created_by_id, company_id
        )
        return product
