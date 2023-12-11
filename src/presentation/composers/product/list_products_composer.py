from src.data.use_cases.product.list_products import ListProductsUseCase
from src.infrastructure.database.repositories.product_repository import (
    ProductRepository,
)
from src.presentation.controllers.product.list_products_controller import (
    ListProductsController,
)
from src.presentation.schemas.product import ProductOut


def list_products_composer(session) -> list[ProductOut] | None:
    repository = ProductRepository(session)
    use_case = ListProductsUseCase(repository)
    controller = ListProductsController(use_case)
    products = controller.handle()
    return products
