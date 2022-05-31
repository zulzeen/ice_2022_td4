import os
from functools import lru_cache

from pydantic import AnyUrl, BaseSettings

class Settings(BaseSettings):
    database_url: AnyUrl = os.environ.get("DATABASE_URL")

@lru_cache()
def get_settings() -> BaseSettings:
    return Settings()