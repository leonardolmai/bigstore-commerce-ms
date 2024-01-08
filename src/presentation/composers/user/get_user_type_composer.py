from src.data.use_cases.user_company.list_all_user_companies import (
    ListAllUserCompaniesUseCase,
)
from src.infrastructure.database.repositories.user_company_repository import (
    UserCompanyRepository,
)
from src.main.settings.config import settings
from src.presentation.controllers.user_company.list_all_user_companies_controller import (
    ListAllUserCompaniesController,
)
from src.presentation.schemas.user import UserTypeOut


def get_user_type_composer(
    session, current_user, current_company
) -> UserTypeOut | None:
    repository = UserCompanyRepository(session)
    use_case = ListAllUserCompaniesUseCase(repository)
    controller = ListAllUserCompaniesController(use_case)
    user_companies = controller.handle(user=current_user, company=current_company)

    if (
        current_user.id == current_company.owner_id
        and current_company.cnpj == settings.COMPANY_CNPJ
    ):
        return {"type": "Bigstore"}

    if user_companies and current_company.cnpj == settings.COMPANY_CNPJ:
        for user_company in user_companies:
            if user_company.is_employee:
                return {"type": "Employee (Bigstore)"}

    if current_user.id == current_company.owner_id:
        return {"type": "Company"}

    if user_companies:
        for user_company in user_companies:
            if (
                user_company.is_employee
                and current_company.id == user_company.company_id
            ):
                return {"type": "Employee"}

    return {"type": "Customer"}
