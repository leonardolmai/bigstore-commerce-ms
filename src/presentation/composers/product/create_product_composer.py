from src.data.use_cases.product.create_product import CreateProductUseCase
from src.infrastructure.database.repositories.product_repository import (
    ProductRepository,
)
from src.presentation.controllers.product.create_product_controller import (
    CreateProductController,
)
from src.presentation.schemas.product import ProductOut


def create_product_composer(
    session, product, created_by_id, company_id
) -> ProductOut | None:
    repository = ProductRepository(session)
    use_case = CreateProductUseCase(repository)
    controller = CreateProductController(use_case)
    company = controller.handle(product, created_by_id, company_id)
    return company
