# pylint: disable=duplicate-code
from src.data.use_cases.product.get_product import GetProductUseCase
from src.data.use_cases.product_image.list_product_images import (
    ListProductImagesUseCaseUseCase,
)
from src.infrastructure.database.repositories.product_image_repository import (
    ProductImageRepository,
)
from src.infrastructure.database.repositories.product_repository import (
    ProductRepository,
)
from src.presentation.controllers.product.get_product_controller import (
    GetProductController,
)
from src.presentation.controllers.product_image.list_product_images_controller import (
    ListProductImagesController,
)
from src.presentation.schemas.product_image import ProductImageOut


def list_product_images_composer(session, id) -> list[ProductImageOut] | None:
    repository = ProductRepository(session)
    use_case = GetProductUseCase(repository)
    controller = GetProductController(use_case)
    product = controller.handle(id)
    if product:
        repository = ProductImageRepository(session)
        use_case = ListProductImagesUseCaseUseCase(repository)
        controller = ListProductImagesController(use_case)
        product_images = controller.handle(product)
        return product_images
    return None
