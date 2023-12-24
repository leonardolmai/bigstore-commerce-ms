from pydantic import BaseModel


class OrderItemOut(BaseModel):
    id: int
    order_id: int
    product_id: int
    name: str
    price: float
    quantity: int


class OrderItemCreate(BaseModel):
    order_id: int | None = None
    product_id: int
    name: str
    price: float
    quantity: int
