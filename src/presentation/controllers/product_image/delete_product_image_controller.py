from src.domain.use_cases.product_image.delete_product_image import (
    DeleteProductImageUseCaseInterface,
)
from src.presentation.schemas.product_image import ProductImageOut


class DeleteProductImageController:
    def __init__(self, use_case: DeleteProductImageUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self, id, product_id) -> ProductImageOut | None:
        response = self.__use_case.execute(id, product_id)
        return response
