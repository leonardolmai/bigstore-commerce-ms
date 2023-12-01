from src.data.use_cases.product.delete_product import DeleteProductUseCase
from src.infrastructure.database.repositories.product_repository import (
    ProductRepository,
)
from src.presentation.controllers.product.delete_product_controller import (
    DeleteProductController,
)
from src.presentation.schemas.product import ProductOut


def delete_product_composer(session, id) -> ProductOut | None:
    repository = ProductRepository(session)
    use_case = DeleteProductUseCase(repository)
    controller = DeleteProductController(use_case)
    product = controller.handle(id)
    return product
