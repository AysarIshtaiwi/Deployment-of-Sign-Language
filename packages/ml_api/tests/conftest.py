import pytest

from ml_api.api.config import TestingConfig
from ml_api.api.app import create_app



@pytest.fixture
def app():
    app=create_app(config_obj=TestingConfig)

    with app.app_context():
        yield app

@pytest.fixture
def flask_test_app(app):
    with app.test_client() as test_client:
        yield test_client
