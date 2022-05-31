from pydantic import BaseModel, constr
from datetime import date

class CoinBaseSchema(BaseModel):
    name_id: str
    name: str
    symbol: str
    first_coin_emitted_on: str | None

class CoinBaseResponseSchema(CoinBaseSchema):
    id: int
