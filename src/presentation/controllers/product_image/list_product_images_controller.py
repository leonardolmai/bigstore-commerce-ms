from src.domain.use_cases.product_image.list_product_images import (
    ListProductImagesUseCaseInterface,
)
from src.presentation.schemas.product_image import ProductImageOut


class ListProductImagesController:
    def __init__(self, use_case: ListProductImagesUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self, product) -> list[ProductImageOut] | None:
        response = self.__use_case.execute(product)
        return response
