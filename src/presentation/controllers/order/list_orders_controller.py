from src.domain.use_cases.order.list_orders import ListOrdersUseCaseInterface
from src.presentation.schemas.order import OrderOut


class ListOrdersController:
    def __init__(self, use_case: ListOrdersUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self) -> list[OrderOut] | None:
        response = self.__use_case.execute()
        return response
