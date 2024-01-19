from unittest.mock import Mock

from src.domain.entities.card import Card
from src.domain.use_cases.card.create_card import CreateCardUseCaseInterface
from src.domain.use_cases.card.delete_card import DeleteCardUseCaseInterface
from src.domain.use_cases.card.get_card import GetCardUseCaseInterface
from src.domain.use_cases.card.list_card import ListCardUseCaseInterface
from src.domain.use_cases.card.update_card import UpdateCardUseCaseInterface
from src.presentation.controllers.card.create_card_controller import (
    CreateCardController,
)
from src.presentation.controllers.card.delete_card_controller import (
    DeleteCardController,
)
from src.presentation.controllers.card.get_card_controller import GetCardController
from src.presentation.controllers.card.list_card_controller import ListCardController
from src.presentation.controllers.card.update_card_controller import (
    UpdateCardController,
)
from tests.utils.test_case_controller import TestCaseControllerBase


class TestUserController(TestCaseControllerBase):
    def test_list_cards_handle_returns_cards(self):
        # Crie um objeto mock para ListCardUseCaseInterface
        list_card_use_case_mock = Mock(spec=ListCardUseCaseInterface)

        # Crie o controlador usando o objeto mock
        list_card_controller = ListCardController(list_card_use_case_mock)

        # Configure o comportamento esperado do método execute no mock
        cards_data = [
            {
                "id": 1,
                "user_id": 1,
                "name": "User 1",
                "number": "12345656",
                "expiration_month": 12,
                "expiration_year": 1998,
                "cvc": "123",
            },
            {
                "id": 2,
                "user_id": 1,
                "name": "User 2",
                "number": "12345657",
                "expiration_month": 11,
                "expiration_year": 2023,
                "cvc": "321",
            },
        ]
        list_card_use_case_mock.execute.return_value = cards_data
        result = list_card_controller.handle(1)
        self.assertEqual(result, cards_data)

    def test_get_card_handle_returns_user(self):
        get_user_use_case_mock = Mock(spec=GetCardUseCaseInterface)
        get_user_controller = GetCardController(get_user_use_case_mock)

        card_data = {
            "id": 1,
            "user_id": 1,
            "name": "User 1",
            "number": "12345656",
            "expiration_month": 12,
            "expiration_year": 1998,
            "cvc": "123",
        }
        get_user_use_case_mock.execute.return_value = card_data

        result = get_user_controller.handle("user1@example.com")
        self.assertEqual(result, card_data)

    def test_delete_card_handle_returns_user(self):
        delete_user_use_case_mock = Mock(spec=DeleteCardUseCaseInterface)
        delete_user_controller = DeleteCardController(delete_user_use_case_mock)

        card_data = {
            "id": 1,
            "user_id": 1,
            "name": "User 1",
            "number": "12345656",
            "expiration_month": 12,
            "expiration_year": 1998,
            "cvc": "123",
        }
        delete_user_use_case_mock.execute.return_value = card_data

        result = delete_user_controller.handle("user1@example.com")
        self.assertEqual(result, card_data)

    def test_create_user_handle_returns_user(self):
        create_card_use_case_mock = Mock(spec=CreateCardUseCaseInterface)
        create_card_controller = CreateCardController(create_card_use_case_mock)

        card_data = Card(
            id=3,
            user_id=2,
            name="user3",
            number="987654321",
            expiration_month="10",
            expiration_year="2023",
            cvc="101",
        )
        create_card_use_case_mock.execute.return_value = card_data

        result = create_card_controller.handle(card_data, card_data.id)
        self.assertEqual(result, card_data)

    def test_update_user_handle_returns_user(self):
        update_card_use_case_mock = Mock(spec=UpdateCardUseCaseInterface)
        update_card_controller = UpdateCardController(update_card_use_case_mock)

        card_data = {
            "id": 1,
            "user_id": 1,
            "name": "User 123",
            "number": "12345656",
            "expiration_month": 12,
            "expiration_year": 1998,
            "cvc": "123",
        }
        update_card_use_case_mock.execute.return_value = card_data

        result = update_card_controller.handle(card_data, card_data["user_id"])
        self.assertEqual(result, card_data)
