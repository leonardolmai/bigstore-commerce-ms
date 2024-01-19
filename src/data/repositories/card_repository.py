from abc import ABC, abstractmethod
from typing import Any

from src.domain.entities.card import Card


class CardRepositoryInterface(ABC):
    @abstractmethod
    def list_card(self, user_id: int) -> list[Card] | None:
        pass

    @abstractmethod
    def get_card(self, id: int) -> Card | None:
        pass

    @abstractmethod
    def create_card(self, card: Card, user_id: int) -> Card | None:
        pass

    @abstractmethod
    def update_card(self, update_fields: dict[str, Any], id: int) -> Card | None:
        pass

    @abstractmethod
    def delete_card(self, id: int) -> bool:
        pass
