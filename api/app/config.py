from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str                       # required: app won't start without it
    gemini_api_key: str = ""                # optional for now
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()                       # one shared object other files import