from pydantic import BaseModel


class Settings(BaseModel):
    api_title: str = "AutonomyX Finder API"
    api_version: str = "0.1.0"
    api_prefix: str = "/o/findr-api"


settings = Settings()
