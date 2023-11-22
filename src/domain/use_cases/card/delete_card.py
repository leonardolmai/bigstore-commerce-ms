from abc import ABC, abstractmethod

from src.domain.entities.card import Card


class DeleteCardUseCaseInterface(ABC):
    @abstractmethod
    def execute(self, id: int) -> Card | None:
        pass
