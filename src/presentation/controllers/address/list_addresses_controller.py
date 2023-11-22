from src.domain.use_cases.address.list_addresses import ListAddressesUseCaseInterface
from src.presentation.schemas.address import AddressOut


class ListAddressesController:
    def __init__(self, use_case: ListAddressesUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self, user_id: int) -> list[AddressOut] | None:
        response = self.__use_case.execute(user_id)
        return response
