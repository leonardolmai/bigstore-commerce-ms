from src.data.repositories.address_repository import AddressRepositoryInterface
from src.domain.entities.address import Address
from src.domain.use_cases.address.list_addresses import ListAddressesUseCaseInterface


class ListAddressessUseCase(ListAddressesUseCaseInterface):
    def __init__(self, address_repository: AddressRepositoryInterface) -> None:
        self.__address_repository = address_repository

    def execute(self, user_id: int) -> list[Address] | None:
        address = self.__address_repository.list_address(user_id)
        return address
