from pydantic import BaseSettings


class Settings(BaseSettings):
    bot_token: str = '123'
    use_redis: bool = False
    #my_tg_cli_id: str

    class Config:
        env_file = "../../.env"
        env_file_encoding = 'utf8'


settings = Settings()
