from src.domain.use_cases.product.list_products import ListProductsUseCaseInterface
from src.presentation.schemas.product import ProductOut


class ListProductsController:
    def __init__(self, use_case: ListProductsUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self) -> list[ProductOut] | None:
        response = self.__use_case.execute()
        return response
