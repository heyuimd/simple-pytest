import pytest


def mul(a: int, b: int) -> int:
    return a * b


@pytest.fixture(autouse=True)
def hello():
    yield

    print("\ndone")


@pytest.fixture
def a():
    return 3


@pytest.fixture
def b():
    return 4


def test_mul(a, b):
    assert mul(a, b) == a * b


@pytest.mark.parametrize("a, b", [(1, 2), (3, 4)])
def test_mul2(a, b):
    assert mul(a, b) == a * b


@pytest.mark.parametrize("a", [1, 2, 3])
@pytest.mark.parametrize("b", [4, 5, 6])
def test_mul3(a, b):
    assert mul(a, b) == a * b
