from src.domain.use_cases.order.get_order import GetOrderUseCaseInterface
from src.presentation.schemas.order import OrderOut


class GetOrderController:
    def __init__(self, use_case: GetOrderUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self, id) -> OrderOut | None:
        response = self.__use_case.execute(id)
        return response
