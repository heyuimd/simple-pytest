import pytest

from app.storage import storage
from app.utils import start_program, stop_program


@pytest.fixture(scope="session", autouse=True)
def program():
    start_program()

    yield

    stop_program()


@pytest.fixture
def clear_storage():
    yield

    storage.clear()
