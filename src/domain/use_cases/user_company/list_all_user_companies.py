from abc import ABC, abstractmethod

from src.domain.entities.user_company import UserCompany


class ListAllUserCompaniesUseCaseInterface(ABC):
    @abstractmethod
    def execute(self, user, company) -> list[UserCompany] | None:
        pass
