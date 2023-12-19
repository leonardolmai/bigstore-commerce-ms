from src.domain.use_cases.order_item.create_order_item import (
    CreateOrderItemUseCaseInterface,
)
from src.presentation.schemas.order_item import OrderItemOut


class CreateOrderItemController:
    def __init__(self, use_case: CreateOrderItemUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self, order_item) -> OrderItemOut | None:
        response = self.__use_case.execute(order_item)
        return response
