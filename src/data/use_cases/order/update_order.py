from typing import Any

from src.data.repositories.order_repository import OrderRepositoryInterface
from src.domain.entities.order import Order
from src.domain.use_cases.order.update_order import UpdateOrderUseCaseInterface


class UpdateOrderUseCase(UpdateOrderUseCaseInterface):
    def __init__(self, order_repository: OrderRepositoryInterface) -> None:
        self.__order_repository = order_repository

    def execute(self, id, update_fields: dict[str, Any]) -> Order | None:
        order = self.__order_repository.update_order(id, update_fields)
        return order
