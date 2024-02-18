from os import getenv

from dotenv import load_dotenv

load_dotenv()


class BaseConfiguration:
    SECRET_KEY = getenv("SECRET_KEY")

    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"

    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = getenv("MAIL_USERNAME")
    MAIL_PASSWORD = getenv("MAIL_APP_PASSWORD")
    MAIL_DEFAULT_SENDER = "noreply@mewi.dev"


class DevelopmentConfiguration(BaseConfiguration):
    DEBUG = True


class ProductionConfiguration(BaseConfiguration):
    JSON_SORT_KEYS = False


class TestingConfiguration(BaseConfiguration):
    TESTING = True


CONFIGURATIONS = {
    "development": DevelopmentConfiguration,
    "production": ProductionConfiguration,
    "testing": TestingConfiguration
}
