# pylint: disable=abstract-class-instantiated
from src.data.use_cases.card.create_card import CreateCardUseCase
from src.infrastructure.database.repositories.card_repository import CardRepository
from src.presentation.controllers.card.create_card_controller import (
    CreateCardController,
)
from src.presentation.schemas.card import CardOut


def create_card_composer(session, card, user_id: int) -> CardOut | None:
    repository = CardRepository(session)
    use_case = CreateCardUseCase(repository)
    controller = CreateCardController(use_case)
    card = controller.handle(card, user_id)
    return card
