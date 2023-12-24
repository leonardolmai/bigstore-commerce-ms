from src.data.use_cases.order.get_order import GetOrderUseCase
from src.infrastructure.database.repositories.order_repository import OrderRepository
from src.presentation.controllers.order.get_order_controller import GetOrderController
from src.presentation.schemas.order import OrderOut


def get_order_composer(session, id) -> OrderOut | None:
    repository = OrderRepository(session)
    use_case = GetOrderUseCase(repository)
    controller = GetOrderController(use_case)
    order = controller.handle(id)

    return order
