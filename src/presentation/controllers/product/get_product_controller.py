from src.domain.use_cases.product.get_product import GetProductUseCaseInterface
from src.presentation.schemas.product import ProductOut


class GetProductController:
    def __init__(self, use_case: GetProductUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self, id) -> ProductOut | None:
        response = self.__use_case.execute(id)
        return response
