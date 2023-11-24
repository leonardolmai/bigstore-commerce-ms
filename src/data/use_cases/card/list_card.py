from src.data.repositories.card_repository import CardRepositoryInterface
from src.domain.entities.card import Card
from src.domain.use_cases.card.list_card import ListCardUseCaseInterface


class ListCardUseCase(ListCardUseCaseInterface):
    def __init__(self, card_repository: CardRepositoryInterface) -> None:
        self.__card_repository = card_repository

    def execute(self, user_id: int) -> list[Card] | None:
        card = self.__card_repository.list_card(user_id)
        return card
