# pylint: disable=unused-argument
from typing import Annotated

from fastapi import APIRouter, Depends, Header, HTTPException, status
from sqlalchemy.orm import Session

from src.infrastructure.database.settings.db_connection import get_db
from src.presentation.composers.order.create_order_composer import create_order_composer
from src.presentation.composers.order.get_order_composer import get_order_composer
from src.presentation.composers.order.list_orders_composer import list_orders_composer
from src.presentation.composers.order.update_order_composer import update_order_composer
from src.presentation.composers.order_item.list_order_items_composer import (
    list_order_items_composer,
)
from src.presentation.dependencies.get_current_company import get_current_company
from src.presentation.dependencies.get_current_user import get_current_user
from src.presentation.schemas.company import CompanyOut
from src.presentation.schemas.order import (
    OrderCreate,
    OrderOut,
    OrderProduct,
    OrderUpdate,
)
from src.presentation.schemas.order_item import OrderItemOut
from src.presentation.schemas.user import UserOut

router = APIRouter(prefix="/orders", tags=["orders"])


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[OrderOut])
def list_orders(
    x_company_cnpj: Annotated[str, Header()],
    current_user: UserOut = Depends(get_current_user),
    # current_company: CompanyOut = Depends(get_current_company),
    session: Session = Depends(get_db),
):
    if current_user:
        orders = list_orders_composer(session)
        if orders:
            return orders
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="Orders not found."
    )


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=OrderOut)
def get_order(
    id: int,
    x_company_cnpj: Annotated[str, Header()],
    current_user: UserOut = Depends(get_current_user),
    session: Session = Depends(get_db),
):
    if current_user:
        order = get_order_composer(session, id)
        if order:
            return order
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Order not found."
    )


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=OrderOut)
def create_order(
    order: OrderCreate,
    order_products: list[OrderProduct],
    address_id: int,
    x_company_cnpj: Annotated[str, Header()],
    card_id: int | None = None,
    current_user: UserOut = Depends(get_current_user),
    current_company: CompanyOut = Depends(get_current_company),
    session: Session = Depends(get_db),
):
    if current_user:
        if order.payment_method == "card" and card_id is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Card ID is required for card payment.",
            )
        order = create_order_composer(
            session,
            order,
            order_products,
            card_id=card_id,
            address_id=address_id,
            user_id=current_user.id,
            company_id=current_company.id,
        )
        if order:
            return order
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT, detail="Order already exists."
    )


@router.patch("/{id}", status_code=status.HTTP_200_OK, response_model=OrderOut)
def update_order(
    id: int,
    order: OrderUpdate,
    x_company_cnpj: Annotated[str, Header()],
    current_user: UserOut = Depends(get_current_user),
    session: Session = Depends(get_db),
):
    order = order.model_dump(exclude_unset=True)
    if current_user:
        order = update_order_composer(session, id, order)
        if order:
            return order
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Order not found."
    )


@router.get(
    "/{id}/order_items/",
    status_code=status.HTTP_200_OK,
    response_model=list[OrderItemOut],
    tags=["order items"],
)
async def list_order_items(
    id: int,
    x_company_cnpj: Annotated[str, Header()],
    current_company: CompanyOut = Depends(get_current_company),
    current_user: UserOut = Depends(get_current_user),
    session: Session = Depends(get_db),
):
    if current_company:
        order_items = list_order_items_composer(session, id)
        return order_items
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="Order items not found."
    )
