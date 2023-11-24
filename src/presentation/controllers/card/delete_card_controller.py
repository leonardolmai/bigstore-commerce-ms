from src.domain.use_cases.card.delete_card import DeleteCardUseCaseInterface
from src.presentation.schemas.card import CardOut


class DeleteCardController:
    def __init__(self, use_case: DeleteCardUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self, id: int) -> CardOut | None:
        response = self.__use_case.execute(id)
        return response
