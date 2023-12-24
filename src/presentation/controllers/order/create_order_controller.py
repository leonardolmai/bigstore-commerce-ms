from src.domain.use_cases.order.create_order import CreateOrderUseCaseInterface
from src.presentation.schemas.order import OrderOut


class CreateOrderController:
    def __init__(self, use_case: CreateOrderUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self, order, user_id, company_id) -> OrderOut | None:
        response = self.__use_case.execute(order, user_id, company_id)
        return response
