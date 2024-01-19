from abc import ABC, abstractmethod
from typing import Any

from src.domain.entities.card import Card


class UpdateCardUseCaseInterface(ABC):
    @abstractmethod
    def execute(self, update_fields: dict[str, Any], id: int) -> Card | None:
        pass
