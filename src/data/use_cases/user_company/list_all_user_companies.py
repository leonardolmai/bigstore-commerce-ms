from src.data.repositories.user_company_repository import UserCompanyRepositoryInterface
from src.domain.entities.user_company import UserCompany
from src.domain.use_cases.user_company.list_all_user_companies import (
    ListAllUserCompaniesUseCaseInterface,
)


class ListAllUserCompaniesUseCase(ListAllUserCompaniesUseCaseInterface):
    def __init__(self, user_company_repository: UserCompanyRepositoryInterface) -> None:
        self.__user_company_repository = user_company_repository

    def execute(self, user, company) -> list[UserCompany] | None:
        user_companies = self.__user_company_repository.list_all_user_companies(
            user, company
        )
        return user_companies
