import pytest

from app.storage import storage
from app.utils import start_program, stop_program

# 공통으로 사용할 fixture는 conftest.py에 정의하자.
# fixture을 import하지 않아도 사용할 수 있도록 pytest가 동작한다.
#  CAUTION: autouse=True 인 경우 주의
#
# Q: fixture의 사용이 암시적이여서 유지 보수가 안되는 거 아닌가?
# A: IDE의 힘을 믿자.


@pytest.fixture(scope="session", autouse=True)
def program():
    start_program()

    yield

    stop_program()


@pytest.fixture
def clear_storage():
    yield

    storage.clear()
