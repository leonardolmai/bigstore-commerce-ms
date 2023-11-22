from abc import ABC, abstractmethod

from src.domain.entities.address import Address


class DeleteAddressUseCaseInterface(ABC):
    @abstractmethod
    def execute(self, id: int) -> Address | None:
        pass
