from src.data.repositories.order_item_repository import OrderItemRepositoryInterface
from src.domain.entities.order_item import OrderItem
from src.domain.use_cases.order_item.create_order_item import (
    CreateOrderItemUseCaseInterface,
)


class CreateOrderItemUseCase(CreateOrderItemUseCaseInterface):
    def __init__(self, order_item_repository: OrderItemRepositoryInterface) -> None:
        self.__order_item_repository = order_item_repository

    def execute(self, order_item: OrderItem) -> OrderItem | None:
        order_item = self.__order_item_repository.create_order_item(order_item)
        return order_item
