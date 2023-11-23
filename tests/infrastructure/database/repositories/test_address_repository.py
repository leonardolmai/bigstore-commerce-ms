from src.infrastructure.database.models.address import Address as AddressModel
from src.infrastructure.database.repositories.address_repository import (
    AddressRepository,
)
from tests.utils.test_case_repository import TestCaseRepositoryBase


class TestAddressRepository(TestCaseRepositoryBase):
    def setUp(self):
        super().setUp()
        self.repo = AddressRepository(self.session_mock)

    def test_list_address_returns_address(self):
        self.session_mock.query.return_value.filter.return_value.all.return_value = [
            {
                "id": 1,
                "user_id": 1,
                "postal_code": "123333",
                "uf": "rn",
                "city": "pau dos ferros",
                "neighborhood": "not",
                "street": "center",
                "number": "123",
                "complement": "complement1",
            },
            {
                "id": 2,
                "user_id": 1,
                "postal_code": "123334",
                "uf": "rn",
                "city": "pau dos ferros",
                "neighborhood": "not1",
                "street": "center2",
                "number": "4321",
                "complement": "complement2",
            },
        ]

        result = self.repo.list_address(2)

        self.session_mock.query.return_value.filter.return_value.all.assert_called_once()
        self.assertEqual(len(result), 2)

    def test_list_address_exception(self):
        self.session_mock.query.side_effect = Exception("Database error")
        result = self.repo.list_address(1)
        self.assertIsNone(result)

    def test_get_address_returns_address(self):
        address_data = (
            {
                "id": 1,
                "user_id": 1,
                "postal_code": "123333",
                "uf": "rn",
                "city": "pau dos ferros",
                "neighborhood": "not",
                "street": "center",
                "number": "123",
                "complement": "complement1",
            },
        )

        self.session_mock.query.return_value.filter.return_value.one_or_none.return_value = (
            address_data
        )

        result = self.repo.get_address(1)
        self.session_mock.query.return_value.filter.return_value.one_or_none.assert_called_once()
        self.assertEqual(result, address_data)

    def test_get_address_exception(self):
        self.session_mock.query.side_effect = Exception("Database error")
        result = self.repo.get_address(1)
        self.assertIsNone(result)

    def test_create_address_returns_address(self):
        address_data = {
            "user_id": 1,
            "postal_code": "123333",
            "uf": "rn",
            "city": "pau dos ferros",
            "neighborhood": "not",
            "street": "center",
            "number": "123",
            "complement": "complement1",
        }
        result = self.repo.create_address(AddressModel(**address_data), user_id=1)

        self.session_mock.add.assert_called_once()
        self.session_mock.commit.assert_called_once()
        self.assertEqual(result.uf, address_data["uf"])
        self.assertEqual(result.number, address_data["number"])

    def test_create_address_exception(self):
        self.session_mock.add.side_effect = Exception("Simulating an exception")
        mock_address = AddressModel(
            postal_code="123333",
            uf="rn",
            city="pau dos ferros",
            neighborhood="not",
            street="center",
            number="123",
            complement="complement2",
        )

        result = self.repo.create_address(mock_address, user_id=0)
        self.assertIsNone(result)

    def test_update_address_returns_address(self):
        address_data = {
            "postal_code": "33222",
            "uf": "rn",
        }

        self.session_mock.query.return_value.filter.return_value.update.return_value = 1
        self.session_mock.query.return_value.filter.return_value.one_or_none.return_value = AddressModel(
            id=1,
            user_id=1,
            postal_code="33222",
            uf="sp",
            city="pau dos ferros",
            neighborhood="not",
            street="center",
            number="123",
            complement="complement1",
        )

        result = self.repo.update_address(4, address_data)
        self.session_mock.query.return_value.filter.return_value.update.assert_called_once_with(
            address_data
        )
        self.session_mock.commit.assert_called_once()

        self.assertEqual(result.postal_code, address_data["postal_code"])

    def test_update_address_returns_none_on_exception(self):
        self.session_mock.query.return_value.filter.return_value.update.side_effect = (
            Exception("Simulating an exception")
        )

        result = self.repo.update_address(1, {"postal_code": "0000000"})

        self.session_mock.query.return_value.filter.assert_called_once()
        self.session_mock.query.return_value.filter.return_value.update.assert_called_once()
        self.session_mock.commit.assert_not_called()
        self.assertIsNone(result)

    def test_delete_address_returns_true(self):
        self.session_mock.query.return_value.filter.return_value.delete.return_value = 1
        result = self.repo.delete_address(1)
        self.session_mock.query.return_value.filter.assert_called_once()
        self.session_mock.query.return_value.filter.return_value.delete.assert_called_once()
        self.session_mock.commit.assert_called_once()
        self.assertTrue(result)

    def test_delete_address_exception(self):
        self.session_mock.query.return_value.filter.return_value.delete.side_effect = (
            Exception("Database error")
        )
        result = self.repo.delete_address(1)
        self.assertFalse(result)
