from abc import ABC, abstractmethod
from typing import Any

from src.domain.entities.product import Product


class UpdateProductUseCaseInterface(ABC):
    @abstractmethod
    def execute(self, id, update_fields: dict[str, Any]) -> Product | None:
        pass
