from src.domain.use_cases.user_company.list_all_user_companies import (
    ListAllUserCompaniesUseCaseInterface,
)
from src.presentation.schemas.user_company import UserCompanyOut


class ListAllUserCompaniesController:
    def __init__(self, use_case: ListAllUserCompaniesUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self, user, company) -> list[UserCompanyOut] | None:
        response = self.__use_case.execute(user, company)
        return response
