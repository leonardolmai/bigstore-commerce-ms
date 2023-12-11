from src.data.use_cases.product.get_product import GetProductUseCase
from src.infrastructure.database.repositories.product_repository import (
    ProductRepository,
)
from src.presentation.controllers.product.get_product_controller import (
    GetProductController,
)
from src.presentation.schemas.product import ProductOut


def get_product_composer(session, id) -> ProductOut | None:
    repository = ProductRepository(session)
    use_case = GetProductUseCase(repository)
    controller = GetProductController(use_case)
    product = controller.handle(id)
    return product
