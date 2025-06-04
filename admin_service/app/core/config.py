# app/core/config.py

from pydantic_settings import BaseSettings
from typing import List, Union
from pydantic import AnyHttpUrl, validator


class Settings(BaseSettings):
    PROJECT_NAME: str = "ZCare Admin Service"
    API_V1_STR: str = "/api/v1"
    
    # CORS settings
    CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    # Database settings
    DB_HOST: str = "admin_postgres"  # Changed from localhost to container name
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "Arunnathan"
    DB_NAME: str = "admin_service"
    DB_PORT: str = "5432"
    DATABASE_URL: str = None

    @validator("DATABASE_URL", pre=True)
    def assemble_db_connection(cls, v: str, values: dict) -> str:
        if isinstance(v, str) and v:
            return v
        return (
            f"postgresql://{values.get('DB_USER')}:{values.get('DB_PASSWORD')}@"
            f"{values.get('DB_HOST')}:{values.get('DB_PORT')}/{values.get('DB_NAME')}"
        )


    class Config:
        env_file = ".env"


# Instantiate settings
settings = Settings()
