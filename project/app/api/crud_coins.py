from app.models.tortoise import Coin

async def get_all() -> list | None:
    coins = await Coin.all().values()
    return coins