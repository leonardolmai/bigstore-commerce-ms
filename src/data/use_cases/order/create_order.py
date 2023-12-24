from src.data.repositories.order_repository import OrderRepositoryInterface
from src.domain.entities.order import Order
from src.domain.use_cases.order.create_order import CreateOrderUseCaseInterface


class CreateOrderUseCase(CreateOrderUseCaseInterface):
    def __init__(self, order_repository: OrderRepositoryInterface) -> None:
        self.__order_repository = order_repository

    def execute(self, order: Order, user_id: int, company_id: int) -> Order | None:
        order = self.__order_repository.create_order(order, user_id, company_id)
        return order
