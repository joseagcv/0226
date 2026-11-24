from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str
    DATABASE_URL: str
    WELCOME_MESSAGE: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
print(settings.APP_NAME)
print(settings.DATABASE_URL)
print(settings.WELCOME_MESSAGE)