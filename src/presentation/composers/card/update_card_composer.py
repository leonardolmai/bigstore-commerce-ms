# pylint: disable=abstract-class-instantiated
from src.data.use_cases.card.update_card import UpdateCardUseCase
from src.infrastructure.database.repositories.card_repository import CardRepository
from src.presentation.controllers.card.update_card_controller import (
    UpdateCardController,
)
from src.presentation.schemas.card import CardOut


def update_card_composer(session, id: int, card) -> CardOut | None:
    repository = CardRepository(session)
    use_case = UpdateCardUseCase(repository)
    controller = UpdateCardController(use_case)
    card = controller.handle(card, id)

    return card
