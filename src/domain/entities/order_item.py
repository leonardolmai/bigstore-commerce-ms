class OrderItem:
    def __init__(
        self,
        id: int,
        order_id: int,
        product_id: int,
        name: str,
        price: float,
        quantity: int,
    ) -> None:
        self.id = id
        self.order_id = order_id
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
