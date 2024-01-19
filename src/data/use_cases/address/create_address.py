from src.data.repositories.address_repository import AddressRepositoryInterface
from src.domain.entities.address import Address
from src.domain.use_cases.address.create_address import CreateAddressUseCaseInterface


class CreateAddressUseCase(CreateAddressUseCaseInterface):
    def __init__(self, address_repository: AddressRepositoryInterface) -> None:
        self.__address_repository = address_repository

    def execute(self, address: Address, user_id: int) -> Address | None:
        print(address, "use case")
        address = self.__address_repository.create_address(address, user_id)
        return address
