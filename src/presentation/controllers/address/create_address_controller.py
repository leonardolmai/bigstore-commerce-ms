from src.domain.use_cases.address.create_address import CreateAddressUseCaseInterface
from src.presentation.schemas.address import AddressOut


class CreateAddressController:
    def __init__(self, use_case: CreateAddressUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self, address, user_id: int) -> AddressOut | None:
        response = self.__use_case.execute(address, user_id)
        return response
