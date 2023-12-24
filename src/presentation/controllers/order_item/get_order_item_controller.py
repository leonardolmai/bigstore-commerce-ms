from src.domain.use_cases.order_item.get_order_item import GetOrderItemUseCaseInterface
from src.presentation.schemas.order_item import OrderItemOut


class GetOrderItemController:
    def __init__(self, use_case: GetOrderItemUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self, id) -> OrderItemOut | None:
        response = self.__use_case.execute(id)
        return response
