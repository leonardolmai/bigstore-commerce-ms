# pylint: disable=duplicate-code

from src.data.use_cases.order.get_order import GetOrderUseCase
from src.data.use_cases.order_item.list_order_items import ListOrderItemsUseCase
from src.infrastructure.database.repositories.order_item_repository import (
    OrderItemRepository,
)
from src.infrastructure.database.repositories.order_repository import OrderRepository
from src.presentation.controllers.order.get_order_controller import GetOrderController
from src.presentation.controllers.order_item.list_order_items_controller import (
    ListOrderItemsController,
)
from src.presentation.schemas.order_item import OrderItemOut


def list_order_items_composer(session, id) -> list[OrderItemOut] | None:
    repository = OrderRepository(session)
    use_case = GetOrderUseCase(repository)
    controller = GetOrderController(use_case)
    order = controller.handle(id)
    if order:
        repository = OrderItemRepository(session)
        use_case = ListOrderItemsUseCase(repository)
        controller = ListOrderItemsController(use_case)
        order_item = controller.handle(order)
        return order_item
    return None
