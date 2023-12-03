from pydantic import BaseModel


class ProductImageOut(BaseModel):
    id: int
    image: str
