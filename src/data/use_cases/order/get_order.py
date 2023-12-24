from src.data.repositories.order_repository import OrderRepositoryInterface
from src.domain.entities.order import Order
from src.domain.use_cases.order.get_order import GetOrderUseCaseInterface


class GetOrderUseCase(GetOrderUseCaseInterface):
    def __init__(self, order_repository: OrderRepositoryInterface) -> None:
        self.__order_repository = order_repository

    def execute(self, id: int) -> Order | None:
        order = self.__order_repository.get_order(id)
        return order
