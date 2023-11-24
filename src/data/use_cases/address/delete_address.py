from src.data.repositories.address_repository import AddressRepositoryInterface
from src.domain.entities.address import Address
from src.domain.use_cases.address.delete_address import DeleteAddressUseCaseInterface


class DeleteAddressUseCase(DeleteAddressUseCaseInterface):
    def __init__(self, address_repository: AddressRepositoryInterface) -> None:
        self.__address_repository = address_repository

    def execute(self, id: str) -> Address | None:
        address = self.__address_repository.delete_address(id)
        return address
