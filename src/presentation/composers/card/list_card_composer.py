# pylint: disable=abstract-class-instantiated
from src.data.use_cases.card.list_card import ListCardUseCase
from src.infrastructure.database.repositories.card_repository import CardRepository
from src.presentation.controllers.card.list_card_controller import ListCardController
from src.presentation.schemas.card import CardOut


def list_card_composer(session, user_id: int) -> CardOut | None:
    repository = CardRepository(session)
    use_case = ListCardUseCase(repository)
    controller = ListCardController(use_case)
    card = controller.handle(user_id)
    return card
