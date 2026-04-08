from pydantic import BaseModel


class Settings(BaseModel):
    api_title: str = "AutonomyX Finder API"
    api_version: str = "0.1.0"
    api_prefix: str = "/o/findr-api"
    allowed_origins: list[str] = [
        "http://localhost:5173",
        "http://localhost:3000",
        "https://www.openautonomyx.com",
    ]


settings = Settings()
