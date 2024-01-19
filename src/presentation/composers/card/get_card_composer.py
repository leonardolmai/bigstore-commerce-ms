# pylint: disable=abstract-class-instantiated
from src.data.use_cases.card.get_card import GetCardUseCase
from src.infrastructure.database.repositories.card_repository import CardRepository
from src.presentation.controllers.card.get_card_controller import GetCardController
from src.presentation.schemas.card import CardOut


def get_card_composer(session, id: int) -> CardOut | None:
    repository = CardRepository(session)
    use_case = GetCardUseCase(repository)
    controller = GetCardController(use_case)
    card = controller.handle(id)
    return card
