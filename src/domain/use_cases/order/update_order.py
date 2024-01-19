from abc import ABC, abstractmethod
from typing import Any

from src.domain.entities.order import Order


class UpdateOrderUseCaseInterface(ABC):
    @abstractmethod
    def execute(self, id, update_fields: dict[str, Any]) -> Order | None:
        pass
