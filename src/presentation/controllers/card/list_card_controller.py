from src.domain.use_cases.card.list_card import ListCardUseCaseInterface
from src.presentation.schemas.card import CardOut


class ListCardController:
    def __init__(self, use_case: ListCardUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self, user_id: int) -> list[CardOut] | None:
        response = self.__use_case.execute(user_id)
        return response
