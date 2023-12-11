from pydantic import BaseModel


class ProductImageOut(BaseModel):
    id: int
    image: str


class ProductImageCreate(BaseModel):
    product_id: int
    image: str
