from src.data.use_cases.product.update_product import UpdateProductUseCase
from src.infrastructure.database.repositories.product_repository import (
    ProductRepository,
)
from src.presentation.controllers.product.update_product_controller import (
    UpdateProductController,
)
from src.presentation.schemas.product import ProductOut


def update_product_composer(session, id, product) -> ProductOut | None:
    repository = ProductRepository(session)
    use_case = UpdateProductUseCase(repository)
    controller = UpdateProductController(use_case)
    product = controller.handle(id, product)
    return product
