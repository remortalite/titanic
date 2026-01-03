from pydantic import BaseModel


class Wallet(BaseModel):
    id: int
    user_id: int
    name: str
    bank: str
    full_sum: int
