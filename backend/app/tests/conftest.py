import pytest
from faker import Faker

from app import create_app
from app.configs import get_config

AZURE_TOKEN = None
fake = Faker()


@pytest.fixture(scope="session")
def app(test_configs):
    application = create_app(test_configs)

    application.app_context().push()
    yield application


@pytest.fixture(scope="session")
def test_configs():
    return get_config("test")


@pytest.fixture(scope="session")
def client(app):
    """A test client for the app."""
    return app.test_client()
