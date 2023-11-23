from unittest.mock import Mock

from src.domain.entities.address import Address
from src.domain.use_cases.address.create_address import CreateAddressUseCaseInterface
from src.domain.use_cases.address.delete_address import DeleteAddressUseCaseInterface
from src.domain.use_cases.address.get_address import GetAddressUseCaseInterface
from src.domain.use_cases.address.list_addresses import ListAddressesUseCaseInterface
from src.domain.use_cases.address.update_address import UpdateAddressUseCaseInterface
from src.presentation.controllers.address.create_address_controller import (
    CreateAddressController,
)
from src.presentation.controllers.address.delete_address_controller import (
    DeleteAddressController,
)
from src.presentation.controllers.address.get_address_controller import (
    GetAddressController,
)
from src.presentation.controllers.address.list_addresses_controller import (
    ListAddressesController,
)
from src.presentation.controllers.address.update_address_controller import (
    UpdateAddressController,
)
from tests.utils.test_case_controller import TestCaseControllerBase


class TestAddressController(TestCaseControllerBase):
    def test_list_address_handle_returns_address(self):
        list_card_use_case_mock = Mock(spec=ListAddressesUseCaseInterface)
        list_card_controller = ListAddressesController(list_card_use_case_mock)

        address_data = [
            {
                "id": 1,
                "user_id": 2,
                "postal_code": "123213",
                "uf": "rn",
                "city": "pau dos ferros",
                "neighborhood": "centro",
                "street": "centro",
                "number": "123",
                "complement": "centro",
            },
            {
                "id": 2,
                "user_id": 2,
                "postal_code": "141414",
                "uf": "rn",
                "city": "pau dos ferros",
                "neighborhood": "centro2",
                "street": "centro2",
                "number": "123",
                "complement": "centro2",
            },
        ]
        list_card_use_case_mock.execute.return_value = address_data
        result = list_card_controller.handle(1)
        self.assertEqual(result, address_data)

    def test_get_address_handle_returns_address(self):
        get_user_use_case_mock = Mock(spec=GetAddressUseCaseInterface)
        get_user_controller = GetAddressController(get_user_use_case_mock)

        address_data = {
            "id": 2,
            "user_id": 2,
            "postal_code": "141414",
            "uf": "rn",
            "city": "pau dos ferros",
            "neighborhood": "centro2",
            "street": "centro2",
            "number": "123",
            "complement": "centro2",
        }
        get_user_use_case_mock.execute.return_value = address_data

        result = get_user_controller.handle("user1@example.com")
        self.assertEqual(result, address_data)

    def test_delete_address_handle_returns_address(self):
        delete_address_use_case_mock = Mock(spec=DeleteAddressUseCaseInterface)
        delete_address_controller = DeleteAddressController(
            delete_address_use_case_mock
        )

        address_data = {
            "id": 2,
            "user_id": 2,
            "postal_code": "141414",
            "uf": "rn",
            "city": "pau dos ferros",
            "neighborhood": "centro2",
            "street": "centro2",
            "number": "123",
            "complement": "centro2",
        }
        delete_address_use_case_mock.execute.return_value = address_data

        result = delete_address_controller.handle(1)
        self.assertEqual(result, address_data)

    def test_create_address_handle_returns_address(self):
        create_address_use_case_mock = Mock(spec=CreateAddressUseCaseInterface)
        create_address_controller = CreateAddressController(
            create_address_use_case_mock
        )

        address_data = Address(
            id=2,
            user_id=2,
            postal_code="141414",
            uf="rn",
            city="pau dos ferros",
            neighborhood="centro2",
            street="centro2",
            number="123",
            complement="centro2",
        )
        create_address_use_case_mock.execute.return_value = address_data

        result = create_address_controller.handle(address_data, address_data.id)
        self.assertEqual(result, address_data)

    def test_update_address_handle_returns_address(self):
        update_address_use_case_mock = Mock(spec=UpdateAddressUseCaseInterface)
        update_address_controller = UpdateAddressController(
            update_address_use_case_mock
        )

        address_data = {
            "id": 2,
            "user_id": 2,
            "postal_code": "141414",
            "uf": "rn",
            "city": "pau dos ferros",
            "neighborhood": "centro2",
            "street": "centro2",
            "number": "123",
            "complement": "centro2",
        }
        update_address_use_case_mock.execute.return_value = address_data

        result = update_address_controller.handle(address_data["user_id"], address_data)
        self.assertEqual(result, address_data)
