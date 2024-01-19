from src.data.use_cases.order.list_orders import ListOrdersUseCase
from src.infrastructure.database.repositories.order_repository import OrderRepository
from src.presentation.controllers.order.list_orders_controller import (
    ListOrdersController,
)
from src.presentation.schemas.order import OrderOut


def list_orders_composer(session) -> list[OrderOut] | None:
    repository = OrderRepository(session)
    use_case = ListOrdersUseCase(repository)
    controller = ListOrdersController(use_case)
    orders = controller.handle()
    return orders
