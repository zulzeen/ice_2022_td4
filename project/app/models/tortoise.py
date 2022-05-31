from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Coin(models.Model):
    name_id = fields.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.name_id}"

    class Meta:
        table="coins"


CoinSchema = pydantic_model_creator(Coin)