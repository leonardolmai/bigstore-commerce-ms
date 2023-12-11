from src.data.use_cases.product.get_product import GetProductUseCase
from src.data.use_cases.product_image.delete_product_image import (
    DeleteProductImageUseCase,
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
from src.presentation.controllers.product_image.delete_product_image_controller import (
    DeleteProductImageController,
)
from src.presentation.schemas.product_image import ProductImageOut


def delete_product_image_composer(session, id, id_image) -> ProductImageOut | None:
    repository = ProductRepository(session)
    use_case = GetProductUseCase(repository)
    controller = GetProductController(use_case)
    product = controller.handle(id)
    if product:
        repository = ProductImageRepository(session)
        use_case = DeleteProductImageUseCase(repository)
        controller = DeleteProductImageController(use_case)
        product_image = controller.handle(
            id=id_image,
            product_id=product.id,
        )
        return product_image
    return None
