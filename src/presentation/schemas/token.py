from pydantic import BaseModel


class TokenOut(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
