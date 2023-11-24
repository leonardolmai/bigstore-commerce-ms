from src.data.repositories.card_repository import CardRepositoryInterface
from src.domain.entities.card import Card
from src.domain.use_cases.card.get_card import GetCardUseCaseInterface


class GetCardUseCase(GetCardUseCaseInterface):
    def __init__(self, card_repository: CardRepositoryInterface) -> None:
        self.__card_repository = card_repository

    def execute(self, id: int) -> Card | None:
        card = self.__card_repository.get_card(id)
        return card
