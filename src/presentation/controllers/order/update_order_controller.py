from src.domain.use_cases.order.update_order import UpdateOrderUseCaseInterface
from src.presentation.schemas.order import OrderOut


class UpdateOrderController:
    def __init__(self, use_case: UpdateOrderUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self, id, order) -> OrderOut | None:
        response = self.__use_case.execute(id, order)
        return response
