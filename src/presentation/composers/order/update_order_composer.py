from src.data.use_cases.order.update_order import UpdateOrderUseCase
from src.infrastructure.database.repositories.order_repository import OrderRepository
from src.presentation.controllers.order.update_order_controller import (
    UpdateOrderController,
)
from src.presentation.schemas.order import OrderOut


def update_order_composer(session, id, order) -> OrderOut | None:
    repository = OrderRepository(session)
    use_case = UpdateOrderUseCase(repository)
    controller = UpdateOrderController(use_case)
    order = controller.handle(id, order)
    return order
