from typing import Any

from src.data.repositories.card_repository import CardRepositoryInterface
from src.domain.entities.card import Card
from src.domain.use_cases.card.update_card import UpdateCardUseCaseInterface


class UpdateCardUseCase(UpdateCardUseCaseInterface):
    def __init__(self, card_repository: CardRepositoryInterface) -> None:
        self.__card_repository = card_repository

    def execute(self, update_fields: dict[str, Any], id: int) -> Card | None:
        card = self.__card_repository.update_card(update_fields, id)
        return card
