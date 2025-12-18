import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME = "Trade Opportunities API"
    ENV = os.getenv("ENV", "DEV")
    DEBUG = os.getenv("DEBUG", "true").lower() == "true"

settings = Settings()
