import pytest

from app.utils import mul


# parametrize을 중복으로 사용해서 다양한 조건을 테스트한다.
#   3 x 3 케이스 테스트
@pytest.mark.parametrize("a", [1, 2, 3])
@pytest.mark.parametrize("b", [3, 20, 100])
def test_mul(a, b):
    assert a * b == mul(a, b)
