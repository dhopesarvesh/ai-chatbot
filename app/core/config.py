from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_SERVER: str
    MYSQL_PORT: str
    MYSQL_DB: str
    
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    GEMINI_API_KEY: str

    @property
    def DATABASE_URL(self) -> str:
        return f"mysql+mysqlconnector://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}@{self.MYSQL_SERVER}:{self.MYSQL_PORT}/{self.MYSQL_DB}"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()