from pydantic import BaseModel


class CardAddValidator(BaseModel):
    user_id: int
    card_number: str
    balance: float
    card_name: str
    expire_date: int
