from abc import ABC, abstractmethod

from src.domain.entities.address import Address


class UpdateAddressUseCaseInterface(ABC):
    @abstractmethod
    def execute(self, id: int, update_fields: dict[str, any]) -> Address | None:
        pass
