from src.domain.use_cases.product.create_product import CreateProductUseCaseInterface
from src.presentation.schemas.product import ProductOut


class CreateProductController:
    def __init__(self, use_case: CreateProductUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self, product, created_by_id, company_id) -> ProductOut | None:
        response = self.__use_case.execute(product, created_by_id, company_id)
        return response
