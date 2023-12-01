from src.domain.use_cases.product.update_product import UpdateProductUseCaseInterface
from src.presentation.schemas.product import ProductOut


class UpdateProductController:
    def __init__(self, use_case: UpdateProductUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self, id, product) -> ProductOut | None:
        response = self.__use_case.execute(id, product)
        return response
