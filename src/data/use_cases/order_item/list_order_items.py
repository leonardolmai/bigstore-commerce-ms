from src.data.repositories.order_item_repository import OrderItemRepositoryInterface
from src.domain.entities.order_item import OrderItem
from src.domain.use_cases.order_item.list_order_items import (
    ListOrderItemsUseCaseInterface,
)


class ListOrderItemsUseCase(ListOrderItemsUseCaseInterface):
    def __init__(self, order_item_repository: OrderItemRepositoryInterface) -> None:
        self.__order_item_repository = order_item_repository

    def execute(self, order) -> list[OrderItem] | None:
        order_items = self.__order_item_repository.list_order_items(order)
        return order_items
