from abc import ABC, abstractmethod

from src.domain.entities.card import Card


class ListCardUseCaseInterface(ABC):
    @abstractmethod
    def execute(self, user_id: int) -> list[Card] | None:
        pass
