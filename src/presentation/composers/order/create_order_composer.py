# pylint: disable=unused-argument
# pylint: disable=too-many-locals
# pylint: disable=too-many-branches
# pylint: disable=too-many-statements
from fastapi import HTTPException, status

from src.data.use_cases.address.get_address import GetAddressUseCase
from src.data.use_cases.card.get_card import GetCardUseCase
from src.data.use_cases.order.create_order import CreateOrderUseCase
from src.data.use_cases.order_item.create_order_item import CreateOrderItemUseCase
from src.data.use_cases.product.get_product import GetProductUseCase
from src.data.use_cases.product.update_product import UpdateProductUseCase
from src.infrastructure.database.repositories.address_repository import (
    AddressRepository,
)
from src.infrastructure.database.repositories.card_repository import CardRepository
from src.infrastructure.database.repositories.order_item_repository import (
    OrderItemRepository,
)
from src.infrastructure.database.repositories.order_repository import OrderRepository
from src.infrastructure.database.repositories.product_repository import (
    ProductRepository,
)
from src.presentation.controllers.address.get_address_controller import (
    GetAddressController,
)
from src.presentation.controllers.card.get_card_controller import GetCardController
from src.presentation.controllers.order.create_order_controller import (
    CreateOrderController,
)
from src.presentation.controllers.order_item.create_order_item_controller import (
    CreateOrderItemController,
)
from src.presentation.controllers.product.get_product_controller import (
    GetProductController,
)
from src.presentation.controllers.product.update_product_controller import (
    UpdateProductController,
)
from src.presentation.schemas.order import OrderCreate, OrderOut
from src.presentation.schemas.order_item import OrderItemCreate


def create_order_composer(
    session, order, order_products, card_id, address_id, user_id, company_id
) -> OrderOut | None:
    try:
        if card_id:
            repository = CardRepository(session)
            use_case = GetCardUseCase(repository)
            controller = GetCardController(use_case)
            card = controller.handle(card_id)
            if not card:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, detail="Card not found"
                )
        repository = AddressRepository(session)
        use_case = GetAddressUseCase(repository)
        controller = GetAddressController(use_case)
        address = controller.handle(address_id)
        if not address:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Address not found"
            )

        order_items_list = []
        total = 0.0

        for order_item_create in order_products:
            product_id = order_item_create.product_id
            quantity = order_item_create.quantity

            repository = ProductRepository(session)
            use_case = GetProductUseCase(repository)
            controller = GetProductController(use_case)
            product = controller.handle(product_id)

            if not product:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Product not found",
                )

            if quantity <= 0:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Invalid quantity for product.",
                )

            if product.quantity >= quantity:
                order_item = OrderItemCreate(
                    order_id=None,
                    product_id=product.id,
                    name=product.name,
                    quantity=quantity,
                    price=product.price,
                )
                order_items_list.append(order_item)

                total += product.price * quantity

                use_case = UpdateProductUseCase(repository)
                controller = UpdateProductController(use_case)
                new_product_quantity = product.quantity - quantity
                product_object = {"quantity": new_product_quantity}
                product = controller.handle(product_id, product_object)

                if not product:
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Product out of stock.",
                    )
            else:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Product out of stock.",
                )

        payment_details = ""

        if order.payment_method == "CARD" and card:
            payment_details = card.number
        elif order.payment_method == "PIX":
            payment_details = "Pix payment"
        elif order.payment_method == "BANK_SLIP":
            payment_details = "Bank Slip payment"

        delivery_address = (
            f"{address.street}, {address.number}, {address.complement}, "
            f"{address.neighborhood}, {address.city}, {address.uf}, {address.postal_code}"
        )

        order = OrderCreate(
            payment_method=order.payment_method,
            payment_details=payment_details,
            delivery_address=delivery_address,
            total=total,
        )

        repository = OrderRepository(session)
        use_case = CreateOrderUseCase(repository)
        controller = CreateOrderController(use_case)
        order = controller.handle(order, user_id, company_id)

        if not order:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Failed to create order.",
            )

        for order_item in order_items_list:
            order_item.order_id = order.id

            repository = OrderItemRepository(session)
            use_case = CreateOrderItemUseCase(repository)
            controller = CreateOrderItemController(use_case)
            order_item = controller.handle(order_item)

            if not order_item:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Failed to create order item.",
                )

        return order
    except Exception as e:
        session.rollback()

        raise e
