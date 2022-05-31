from pydantic import BaseModel, constr

class CoinBaseSchema(BaseModel):
    name_id: str

class CoinBaseResponseSchema(CoinBaseSchema):
    id: int
