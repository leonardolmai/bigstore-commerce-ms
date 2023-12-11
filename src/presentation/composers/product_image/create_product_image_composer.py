from src.data.use_cases.product.get_product import GetProductUseCase
from src.data.use_cases.product_image.create_product_image import (
    CreateProductImageUseCase,
)
from src.infrastructure.database.repositories.product_image_repository import (
    ProductImageRepository,
)

# pylint: disable=duplicate-code
from src.infrastructure.database.repositories.product_repository import (
    ProductRepository,
)
from src.presentation.controllers.product.get_product_controller import (
    GetProductController,
)
from src.presentation.controllers.product_image.create_product_image_controller import (
    CreateProductImageController,
)
from src.presentation.schemas.product_image import ProductImageCreate, ProductImageOut


def create_product_image_composer(session, id, image) -> ProductImageOut | None:
    repository = ProductRepository(session)
    use_case = GetProductUseCase(repository)
    controller = GetProductController(use_case)
    product = controller.handle(id)
    if product:
        repository = ProductImageRepository(session)
        use_case = CreateProductImageUseCase(repository)
        controller = CreateProductImageController(use_case)
        product_image = ProductImageCreate(product_id=product.id, image=image)
        product_image = controller.handle(product_image)

        return product_image
    return None
