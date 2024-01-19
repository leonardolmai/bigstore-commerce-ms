from src.data.use_cases.address.update_address import UpdateAddressesUseCase
from src.infrastructure.database.repositories.address_repository import (
    AddressRepository,
)
from src.presentation.controllers.address.update_address_controller import (
    UpdateAddressController,
)
from src.presentation.schemas.address import AddressOut


def update_address_composer(session, id: int, address) -> AddressOut | None:
    repository = AddressRepository(session)
    use_case = UpdateAddressesUseCase(repository)
    controller = UpdateAddressController(use_case)
    address = controller.handle(id, address)
    return address
