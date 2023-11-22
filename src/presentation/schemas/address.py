from pydantic import BaseModel


class AddressCreate(BaseModel):
    postal_code: str
    uf: str
    city: str
    neighborhood: str
    street: str
    number: str
    complement: str


class AddressUpdate(BaseModel):
    postal_code: str | None = None
    uf: str | None = None
    city: str | None = None
    neighborhood: str | None = None
    street: str | None = None
    number: str | None = None
    complement: str | None = None


class AddressOut(BaseModel):
    id: int
    user_id: int
    postal_code: str
    uf: str
    city: str
    neighborhood: str
    street: str
    number: str
    complement: str
