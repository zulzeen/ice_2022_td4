from app.api import crud_coins
from fastapi import APIRouter, HTTPException, Path
from app.models.pydantic import CoinBaseResponseSchema, CoinBaseSchema

router = APIRouter()

@router.get("/", response_model=list[CoinBaseResponseSchema])
async def read_all_coins() -> list[CoinBaseResponseSchema]:
    return await crud_coins.get_all()


@router.post("/", status_code=201)
async def create_coin(payload: CoinBaseSchema) -> CoinBaseResponseSchema:
    coin = await crud_coins.post(payload)
    return coin