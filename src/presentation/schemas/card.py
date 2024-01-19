from pydantic import BaseModel


class CardCreate(BaseModel):
    name: str
    number: str
    expiration_month: str
    expiration_year: str
    cvc: str


class CardUpdate(BaseModel):
    name: str | None = None
    number: str | None = None
    expiration_month: str | None = None
    expiration_year: str | None = None
    cvc: str | None = None


class CardOut(BaseModel):
    name: str
    number: str
    expiration_month: str
    expiration_year: str
    cvc: str
