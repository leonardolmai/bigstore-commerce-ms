from src.domain.use_cases.address.update_address import UpdateAddressUseCaseInterface
from src.presentation.schemas.address import AddressOut


class UpdateAddressController:
    def __init__(self, use_case: UpdateAddressUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self, id: int, address) -> AddressOut | None:
        response = self.__use_case.execute(id, address)
        return response
