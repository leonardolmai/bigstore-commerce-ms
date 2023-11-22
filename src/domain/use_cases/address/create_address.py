from abc import ABC, abstractmethod

from src.domain.entities.address import Address


class CreateAddressUseCaseInterface(ABC):
    @abstractmethod
    def execute(self, address: Address, user_id: int) -> Address | None:
        pass
