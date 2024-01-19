from abc import ABC, abstractmethod

from src.domain.entities.address import Address


class GetAddressUseCaseInterface(ABC):
    @abstractmethod
    def execute(self, id: int) -> Address:
        pass
