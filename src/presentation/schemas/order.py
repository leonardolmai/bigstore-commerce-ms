from datetime import datetime

from pydantic import BaseModel


class OrderProduct(BaseModel):
    product_id: int
    quantity: int


class OrderCreate(BaseModel):
    payment_method: str
    payment_details: str | None = None
    delivery_address: str | None = None
    total: float | None = None


class OrderUpdate(BaseModel):
    status: str | None = None


class OrderOut(BaseModel):
    id: int
    user_id: int
    company_id: int
    status: str
    created_at: datetime
    payment_method: str
    payment_details: str
    delivery_address: str
    total: float
