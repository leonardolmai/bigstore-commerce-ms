# pylint: disable=unused-argument
from typing import Annotated

from fastapi import APIRouter, Depends, Header, HTTPException, status
from sqlalchemy.orm import Session

from src.infrastructure.database.settings.db_connection import get_db
from src.presentation.composers.product.create_product_composer import (
    create_product_composer,
)
from src.presentation.composers.product.delete_product_composer import (
    delete_product_composer,
)
from src.presentation.composers.product.get_product_composer import get_product_composer
from src.presentation.composers.product.list_products_composer import (
    list_products_composer,
)
from src.presentation.composers.product.update_product_composer import (
    update_product_composer,
)
from src.presentation.dependencies.get_current_company import get_current_company
from src.presentation.dependencies.get_current_user import get_current_user
from src.presentation.schemas.company import CompanyOut
from src.presentation.schemas.product import ProductCreate, ProductOut, ProductUpdate
from src.presentation.schemas.user import UserOut

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[ProductOut])
def list_products(
    x_company_cnpj: Annotated[str, Header()],
    current_user: UserOut = Depends(get_current_user),
    # current_company: CompanyOut = Depends(get_current_company),
    session: Session = Depends(get_db),
):
    if current_user:
        products = list_products_composer(session)
        if products:
            return products
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="Products not found."
    )


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=ProductOut)
def get_product(
    id: int,
    x_company_cnpj: Annotated[str, Header()],
    current_user: UserOut = Depends(get_current_user),
    session: Session = Depends(get_db),
):
    if current_user:
        product = get_product_composer(session, id)
        if product:
            return product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Product not found."
    )


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ProductOut)
def create_product(
    product: ProductCreate,
    x_company_cnpj: Annotated[str, Header()],
    current_user: UserOut = Depends(get_current_user),
    current_company: CompanyOut = Depends(get_current_company),
    session: Session = Depends(get_db),
):
    if current_user:
        product = create_product_composer(
            session,
            product,
            created_by_id=current_user.id,
            company_id=current_company.id,
        )
        if product:
            return product
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT, detail="Product already exists."
    )


@router.patch("/{id}", status_code=status.HTTP_200_OK, response_model=ProductOut)
def update_product(
    id: int,
    product: ProductUpdate,
    x_company_cnpj: Annotated[str, Header()],
    current_user: UserOut = Depends(get_current_user),
    session: Session = Depends(get_db),
):
    product = product.model_dump(exclude_unset=True)
    if current_user:
        product = update_product_composer(session, id, product)
        if product:
            return product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Product not found."
    )


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(
    id: int,
    x_company_cnpj: Annotated[str, Header()],
    current_user: UserOut = Depends(get_current_user),
    session: Session = Depends(get_db),
):
    if current_user:
        product = delete_product_composer(session, id)
    if product:
        return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Product not found."
    )
