import pytest

from gewebehaken.app import create_app


@pytest.fixture(scope='session')
def client():
    app = create_app()
    return app.test_client()
