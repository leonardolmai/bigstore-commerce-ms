from src.data.repositories.product_image_repository import (
    ProductImageRepositoryInterface,
)
from src.domain.entities.product_image import ProductImage
from src.domain.use_cases.product_image.list_product_images import (
    ListProductImagesUseCaseInterface,
)


class ListProductImagesUseCaseUseCase(ListProductImagesUseCaseInterface):
    def __init__(
        self, product_image_repository: ProductImageRepositoryInterface
    ) -> None:
        self.__product_image_repository = product_image_repository

    def execute(self, product) -> list[ProductImage] | None:
        product_images = self.__product_image_repository.list_product_images(product)
        return product_images
