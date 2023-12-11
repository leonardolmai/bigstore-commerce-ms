from src.data.repositories.product_image_repository import (
    ProductImageRepositoryInterface,
)
from src.domain.entities.product_image import ProductImage
from src.domain.use_cases.product_image.delete_product_image import (
    DeleteProductImageUseCaseInterface,
)


class DeleteProductImageUseCase(DeleteProductImageUseCaseInterface):
    def __init__(
        self, product_image_repository: ProductImageRepositoryInterface
    ) -> None:
        self.__product_image_repository = product_image_repository

    def execute(self, id: int, product_id: int) -> ProductImage | None:
        product_image = self.__product_image_repository.delete_product_image(
            id, product_id
        )
        return product_image
