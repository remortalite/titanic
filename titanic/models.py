from pydantic import BaseModel


class Wallet(BaseModel):
    id: int
    user: str
    name: str
    bank: str
    full_sum: int
