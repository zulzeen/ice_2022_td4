from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Coin(models.Model):
    name_id = fields.CharField(max_length=50, unique=True)
    name = fields.CharField(max_length=50, unique=True)
    symbol = fields.CharField(max_length=10, unique=True)
    first_coin_emitted_on = fields.CharField(max_length=50, null=True)

    def __str__(self):
        return f"{self.name_id}"

    class Meta:
        table="coins"


CoinSchema = pydantic_model_creator(Coin)