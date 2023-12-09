from src.data.repositories.product_image_repository import (
    ProductImageRepositoryInterface,
)
from src.domain.entities.product_image import ProductImage
from src.domain.use_cases.product_image.create_product_image import (
    CreateProductImageUseCaseInterface,
)


class CreateProductImageUseCase(CreateProductImageUseCaseInterface):
    def __init__(
        self, product_image_repository: ProductImageRepositoryInterface
    ) -> None:
        self.__product_image_repository = product_image_repository

    def execute(self, product_image: ProductImage) -> ProductImage | None:
        product_image = self.__product_image_repository.create_product_image(
            product_image
        )
        return product_image
