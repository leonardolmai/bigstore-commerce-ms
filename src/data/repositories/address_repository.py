from abc import ABC, abstractmethod
from typing import Any

from src.domain.entities.address import Address


class AddressRepositoryInterface(ABC):
    @abstractmethod
    def list_address(self, user_id: int) -> list[Address] | None:
        pass

    @abstractmethod
    def get_address(self, id: int) -> Address | None:
        pass

    @abstractmethod
    def create_address(self, address: Address, user_id: int) -> Address | None:
        pass

    @abstractmethod
    def update_address(self, id: int, update_fields: dict[str, Any]) -> Address | None:
        pass

    @abstractmethod
    def delete_address(self, id: int) -> bool:
        pass
