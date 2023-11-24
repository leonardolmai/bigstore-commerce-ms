# pylint: disable=unused-argument
from typing import Annotated

from fastapi import APIRouter, Depends, Header, HTTPException, status
from sqlalchemy.orm import Session

from src.infrastructure.database.settings.db_connection import get_db
from src.presentation.composers.card.create_card_composer import create_card_composer
from src.presentation.composers.card.delete_card_composer import delete_card_composer
from src.presentation.composers.card.get_card_composer import get_card_composer
from src.presentation.composers.card.list_card_composer import list_card_composer
from src.presentation.composers.card.update_card_composer import update_card_composer
from src.presentation.dependencies.get_current_user import get_current_user
from src.presentation.schemas.card import CardCreate, CardOut, CardUpdate
from src.presentation.schemas.user import UserOut

router = APIRouter(prefix="/cards", tags=["cards"])


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[CardOut])
def list_cards(
    x_company_cnpj: Annotated[str, Header()],
    current_user: UserOut = Depends(get_current_user),
    session: Session = Depends(get_db),
):
    cards = list_card_composer(session, current_user.id)
    if cards:
        return cards
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="List cards not found."
    )


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=CardOut)
def get_card(
    id: int,
    x_company_cnpj: Annotated[str, Header()],
    current_user: UserOut = Depends(get_current_user),
    session: Session = Depends(get_db),
):
    address = get_card_composer(session, id)
    if address:
        return address
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="get-address for id, not found."
    )


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CardOut)
def create_card(
    card: CardCreate,
    x_company_cnpj: Annotated[str, Header()],
    current_user: UserOut = Depends(get_current_user),
    session: Session = Depends(get_db),
):
    card = create_card_composer(session, card, current_user.id)

    if card:
        return card
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT, detail="Card already exists."
    )


@router.patch("/{id}", status_code=status.HTTP_200_OK, response_model=CardOut)
def update_card(
    id: int,
    card: CardUpdate,
    x_company_cnpj: Annotated[str, Header()],
    current_user: UserOut = Depends(get_current_user),
    session: Session = Depends(get_db),
):
    card = card.model_dump(exclude_unset=True)
    card = update_card_composer(session, id, card)
    if card:
        return card
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Update Card, not found."
    )


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_card(
    id: int,
    x_company_cnpj: Annotated[str, Header()],
    current_user: UserOut = Depends(get_current_user),
    session: Session = Depends(get_db),
):
    card = delete_card_composer(session, id)
    if card:
        return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Delete Card not found."
    )
