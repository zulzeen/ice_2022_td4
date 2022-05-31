from app.models.tortoise import Coin
from app.models.pydantic import CoinBaseSchema, CoinBaseResponseSchema


async def get_all() -> list | None:
    coins = await Coin.all().values()
    return coins

async def post(payload: CoinBaseSchema) -> CoinBaseResponseSchema:
    if first_coin_emitted_on := payload.first_coin_emitted_on:
        coin = Coin(name_id=payload.name_id,
                    name=payload.name,
                    symbol=payload.symbol,
                    first_coin_emitted_on=first_coin_emitted_on)
    else:
        coin = Coin(name_id=payload.name_id,
                    name=payload.name,
                    symbol=payload.symbol)
    await coin.save()
    return coin