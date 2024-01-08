# pylint: disable=unused-argument
from typing import Annotated

from fastapi import APIRouter, Depends, Header, HTTPException, status
from sqlalchemy.orm import Session

from src.infrastructure.database.settings.db_connection import get_db
from src.presentation.composers.address.create_address_composer import (
    create_address_composer,
)
from src.presentation.composers.address.delete_address_composer import (
    delete_address_composer,
)
from src.presentation.composers.address.get_address_composer import get_address_composer
from src.presentation.composers.address.list_addresses_composer import (
    list_addresses_composer,
)
from src.presentation.composers.address.update_address_composer import (
    update_address_composer,
)
from src.presentation.dependencies.get_current_user import get_current_user
from src.presentation.schemas.address import AddressCreate, AddressOut, AddressUpdate
from src.presentation.schemas.user import UserOut

router = APIRouter(prefix="/addresses", tags=["addresses"])

@router.get("/", status_code=status.HTTP_200_OK, response_model=list[AddressOut])
def list_addresses(
    x_company_cnpj: Annotated[str, Header()],
    current_user: UserOut = Depends(get_current_user),
    session: Session = Depends(get_db),
):
    address = list_addresses_composer(session, current_user.id)
    if address:
        return address
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="List addresses not found."
    )

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=AddressOut)
def get_address(
    id: int,
    x_company_cnpj: Annotated[str, Header()],
    current_user: UserOut = Depends(get_current_user),
    session: Session = Depends(get_db),
):
    address = get_address_composer(session, id)
    if address:
        return address
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="get-address for id, not found."
    )


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=AddressOut)
def create_address(
    address: AddressCreate,
    x_company_cnpj: Annotated[str, Header()],
    current_user: UserOut = Depends(get_current_user),
    session: Session = Depends(get_db),
):
    address = create_address_composer(session, address, current_user.id)
    if address:
        return address
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="Address already exists or not found.",
    )


@router.patch("/{id}", status_code=status.HTTP_200_OK, response_model=AddressOut)
def update_address(
    id: int,
    address: AddressUpdate,
    x_company_cnpj: Annotated[str, Header()],
    current_user: UserOut = Depends(get_current_user),
    session: Session = Depends(get_db),
):
    # user  = current_user.id
    address = address.model_dump(exclude_unset=True)
    address = update_address_composer(session, id, address)
    if address:
        return address
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Update Address, not found."
    )


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_address(
    id: int,
    x_company_cnpj: Annotated[str, Header()],
    current_user: UserOut = Depends(get_current_user),
    session: Session = Depends(get_db),
):
    # user  = current_user.id
    address = delete_address_composer(session, id)
    if address:
        return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Delete address not found."
    )
