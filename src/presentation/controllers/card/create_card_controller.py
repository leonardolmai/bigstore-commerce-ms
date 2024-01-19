from src.domain.use_cases.card.create_card import CreateCardUseCaseInterface
from src.presentation.schemas.card import CardOut


class CreateCardController:
    def __init__(self, use_case: CreateCardUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self, card, user_id: int) -> CardOut | None:
        response = self.__use_case.execute(card, user_id)
        return response
