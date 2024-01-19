from src.domain.use_cases.address.get_address import GetAddressUseCaseInterface
from src.presentation.schemas.address import AddressOut


class GetAddressController:
    def __init__(self, use_case: GetAddressUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self, id: int) -> AddressOut:
        response = self.__use_case.execute(id)
        return response
