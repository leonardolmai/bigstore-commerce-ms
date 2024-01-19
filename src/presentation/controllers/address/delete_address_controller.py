from src.domain.use_cases.address.delete_address import DeleteAddressUseCaseInterface
from src.presentation.schemas.address import AddressOut


class DeleteAddressController:
    def __init__(self, use_case: DeleteAddressUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self, id: int) -> AddressOut | None:
        response = self.__use_case.execute(id)
        return response
