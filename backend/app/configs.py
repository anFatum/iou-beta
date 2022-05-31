import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), verbose=True)
DEFAULT_CONFIG = None


class Configs:
    DEBUG = False
    ENVIRONMENT = "production"

    SECRET_KEY = os.getenv("SECRET_KEY", "secret")
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*").split(",")


class DevelopmentConfigs(Configs):
    DEBUG = True
    ENVIRONMENT = "development"


class TestingConfigs(Configs):
    DEBUG = True
    ENVIRONMENT = "testing"


class ProductionConfigs(Configs):
    DEBUG = False
    ENVIRONMENT = "production"


_CONFIG_DICT = {
    "dev": DevelopmentConfigs,
    "prod": ProductionConfigs,
    "test": TestingConfigs
}


def get_config(config: str = "dev"):
    try:
        global DEFAULT_CONFIG
        DEFAULT_CONFIG = DEFAULT_CONFIG if DEFAULT_CONFIG is not None \
            else _CONFIG_DICT[config]
        return DEFAULT_CONFIG
    except KeyError:
        raise KeyError("No environment configs found")
