from typing import Any

from src.data.repositories.address_repository import AddressRepositoryInterface
from src.domain.entities.address import Address
from src.domain.use_cases.address.update_address import UpdateAddressUseCaseInterface


class UpdateAddressesUseCase(UpdateAddressUseCaseInterface):
    def __init__(self, address_repository: AddressRepositoryInterface) -> None:
        self.__address_repository = address_repository

    def execute(self, id: int, update_fields: dict[str, Any]) -> Address | None:
        address = self.__address_repository.update_address(id, update_fields)
        return address
