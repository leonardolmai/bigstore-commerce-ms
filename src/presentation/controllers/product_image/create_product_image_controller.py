from src.domain.use_cases.product_image.create_product_image import (
    CreateProductImageUseCaseInterface,
)
from src.presentation.schemas.product_image import ProductImageOut


class CreateProductImageController:
    def __init__(self, use_case: CreateProductImageUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self, product_image) -> ProductImageOut | None:
        response = self.__use_case.execute(product_image)
        return response
