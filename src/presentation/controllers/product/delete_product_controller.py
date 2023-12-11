from src.domain.use_cases.product.delete_product import DeleteProductUseCaseInterface
from src.presentation.schemas.product import ProductOut


class DeleteProductController:
    def __init__(self, use_case: DeleteProductUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self, id) -> ProductOut | None:
        response = self.__use_case.execute(id)
        return response
