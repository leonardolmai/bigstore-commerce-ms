from src.domain.use_cases.order_item.list_order_items import (
    ListOrderItemsUseCaseInterface,
)
from src.presentation.schemas.order_item import OrderItemOut


class ListOrderItemsController:
    def __init__(self, use_case: ListOrderItemsUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self, order) -> list[OrderItemOut] | None:
        response = self.__use_case.execute(order)
        return response
