from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    price: float
    quantity: int
    category: str
    description: str | None = None


class ProductUpdate(BaseModel):
    name: str | None = None
    price: float | None = None
    quantity: int | None = None
    category: str | None = None
    description: str | None = None
    is_approved: bool | None = None


class ProductOut(BaseModel):
    id: int
    name: str
    price: float
    quantity: int
    created_by_id: int
    company_id: int
    category: str
    description: str | None
    is_approved: bool
