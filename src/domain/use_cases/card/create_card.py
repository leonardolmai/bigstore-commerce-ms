from abc import ABC, abstractmethod

from src.domain.entities.card import Card


class CreateCardUseCaseInterface(ABC):
    @abstractmethod
    def execute(self, card: Card, user_id: int) -> Card | None:
        pass
