from src.data.use_cases.address.list_addresses import ListAddressessUseCase
from src.infrastructure.database.repositories.address_repository import (
    AddressRepository,
)
from src.presentation.controllers.address.list_addresses_controller import (
    ListAddressesController,
)
from src.presentation.schemas.address import AddressOut


def list_addresses_composer(session, user_id: int) -> list[AddressOut] | None:
    repository = AddressRepository(session)
    use_case = ListAddressessUseCase(repository)
    controller = ListAddressesController(use_case)
    address = controller.handle(user_id)
    return address
