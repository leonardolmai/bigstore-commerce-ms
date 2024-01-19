from src.data.repositories.order_repository import OrderRepositoryInterface
from src.domain.entities.order import Order
from src.domain.use_cases.order.list_orders import ListOrdersUseCaseInterface


class ListOrdersUseCase(ListOrdersUseCaseInterface):
    def __init__(self, order_repository: OrderRepositoryInterface) -> None:
        self.__order_repository = order_repository

    def execute(self) -> list[Order] | None:
        orders = self.__order_repository.list_orders()
        return orders
