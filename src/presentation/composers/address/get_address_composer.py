from src.data.use_cases.address.get_address import GetAddressUseCase
from src.infrastructure.database.repositories.address_repository import (
    AddressRepository,
)
from src.presentation.controllers.address.get_address_controller import (
    GetAddressController,
)
from src.presentation.schemas.address import AddressOut


def get_address_composer(session, id) -> AddressOut | None:
    repository = AddressRepository(session)
    use_case = GetAddressUseCase(repository)
    controller = GetAddressController(use_case)
    address = controller.handle(id)
    return address
