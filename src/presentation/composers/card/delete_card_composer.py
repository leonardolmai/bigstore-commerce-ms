# pylint: disable=abstract-class-instantiated
from src.data.use_cases.card.delete_card import DeleteCardUseCase
from src.infrastructure.database.repositories.card_repository import CardRepository
from src.presentation.controllers.card.delete_card_controller import (
    DeleteCardController,
)
from src.presentation.schemas.card import CardOut


def delete_card_composer(session, id: int) -> CardOut | None:
    repository = CardRepository(session)
    use_case = DeleteCardUseCase(repository)
    controller = DeleteCardController(use_case)
    card = controller.handle(id)
    return card
