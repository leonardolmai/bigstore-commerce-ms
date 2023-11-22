from src.data.use_cases.address.create_address import CreateAddressUseCase
from src.infrastructure.database.repositories.address_repository import (
    AddressRepository,
)
from src.presentation.controllers.address.create_address_controller import (
    CreateAddressController,
)
from src.presentation.schemas.address import AddressOut


def create_address_composer(session, address, user_id: int) -> AddressOut | None:
    repository = AddressRepository(session)
    use_case = CreateAddressUseCase(repository)
    controller = CreateAddressController(use_case)
    address = controller.handle(address, user_id)
    print(address)
    return address
