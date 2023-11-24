from src.infrastructure.database.models.card import Card as CardModel
from src.infrastructure.database.repositories.card_repository import CardRepository
from tests.utils.test_case_repository import TestCaseRepositoryBase


class TestUserRepository(TestCaseRepositoryBase):
    def setUp(self):
        super().setUp()
        self.repo = CardRepository(self.session_mock)

    def test_list_card_returns_cards(self):
        self.session_mock.query.return_value.filter.return_value.all.return_value = [
            {
                "id": 1,
                "user_id": 1,
                "name": "user1",
                "number": "12345678",
                "expiration_month": "12",
                "expiration_year": "1998",
                "cvc": "123",
            },
            {
                "id": 1,
                "user_id": 2,
                "name": "user1",
                "number": "756231",
                "expiration_month": "11",
                "expiration_year": "2023",
                "cvc": "123",
            },
        ]

        result = self.repo.list_card(2)

        self.session_mock.query.return_value.filter.return_value.all.assert_called_once()
        self.assertEqual(len(result), 2)

    def test_list_card_exception(self):
        self.session_mock.query.side_effect = Exception("Database error")
        result = self.repo.list_card(1)
        self.assertIsNone(result)

    def test_get_card_returns_card(self):
        # Dados do cartão
        card_data = {
            "id": 1,
            "user_id": 1,
            "name": "user1",
            "number": "12345678",
            "expiration_month": "12",
            "expiration_year": "1998",
            "cvc": "123",
        }

        self.session_mock.query.return_value.filter.return_value.one_or_none.return_value = (
            card_data
        )

        result = self.repo.get_card(1)
        self.session_mock.query.return_value.filter.return_value.one_or_none.assert_called_once()
        self.assertEqual(result, card_data)

    def test_get_card_exception(self):
        self.session_mock.query.side_effect = Exception("Database error")
        result = self.repo.get_card(1)
        self.assertIsNone(result)

    def test_create_card_returns_card(self):
        card_data = {
            "name": "user1",
            "number": "40028922",
            "expiration_month": "11",
            "expiration_year": "2012",
            "cvc": "222",
        }
        result = self.repo.create_card(CardModel(**card_data), user_id=1)

        self.session_mock.add.assert_called_once()
        self.session_mock.commit.assert_called_once()
        self.assertEqual(result.name, card_data["name"])
        self.assertEqual(result.number, card_data["number"])

    def test_create_card_exception(self):
        self.session_mock.add.side_effect = Exception("Simulating an exception")
        mock_card = CardModel(
            name="user1",
            number="40028922",
            expiration_month="11",
            expiration_year="2012",
            cvc="222",
        )

        result = self.repo.create_card(mock_card, user_id=0)
        self.assertIsNone(result)

    def test_update_card_returns_card(self):
        card_data = {"name": "user1", "cvc": "123"}

        self.session_mock.query.return_value.filter.return_value.update.return_value = 1
        self.session_mock.query.return_value.filter.return_value.one_or_none.return_value = CardModel(
            id=1,
            user_id=1,
            name="user1",
            number="12345678",
            expiration_month="12",
            expiration_year="1998",
            cvc="222",
        )

        result = self.repo.update_card(card_data, 1)
        self.session_mock.query.return_value.filter.return_value.update.assert_called_once_with(
            card_data
        )
        self.session_mock.commit.assert_called_once()

        self.assertEqual(result.name, "user1")

    def test_update_card_returns_none_on_exception(self):
        self.session_mock.query.return_value.filter.return_value.update.side_effect = (
            Exception("Simulating an exception")
        )

        result = self.repo.update_card({"name": "Novo Nome"}, 1)

        self.session_mock.query.return_value.filter.assert_called_once()
        self.session_mock.query.return_value.filter.return_value.update.assert_called_once()
        self.session_mock.commit.assert_not_called()
        self.assertIsNone(result)

    def test_delete_card_returns_true(self):
        self.session_mock.query.return_value.filter.return_value.delete.return_value = 1
        result = self.repo.delete_card(1)
        self.session_mock.query.return_value.filter.assert_called_once()
        self.session_mock.query.return_value.filter.return_value.delete.assert_called_once()
        self.session_mock.commit.assert_called_once()
        self.assertTrue(result)

    def test_delete_card_exception(self):
        self.session_mock.query.return_value.filter.return_value.delete.side_effect = (
            Exception("Database error")
        )
        result = self.repo.delete_card(1)
        self.assertFalse(result)
