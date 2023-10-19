import pytest

from app.utils import mul


@pytest.mark.parametrize("a", [1, 2, 3])
@pytest.mark.parametrize("b", [3, 20, 100])
def test_mul(a, b):
    assert a * b == mul(a, b)
