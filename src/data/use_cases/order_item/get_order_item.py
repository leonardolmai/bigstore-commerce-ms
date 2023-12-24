from src.data.repositories.order_item_repository import OrderItemRepositoryInterface
from src.domain.entities.order_item import OrderItem
from src.domain.use_cases.order_item.get_order_item import GetOrderItemUseCaseInterface


class GetOrderItemUseCase(GetOrderItemUseCaseInterface):
    def __init__(self, order_item_repository: OrderItemRepositoryInterface) -> None:
        self.__order_item_repository = order_item_repository

    def execute(self, id: int) -> OrderItem | None:
        order_item = self.__order_item_repository.get_order_item(id)
        return order_item
