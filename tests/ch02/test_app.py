import pytest

from app.entity import Robot
from app.exceptions import NotFoundEntity, DuplicateEntity
from app.storage import storage
from app.utils import start_program, stop_program, mul


# scope을 통해 fixture의 생명주기 관리
#   1. session: 테스트 시작부터 끝까지
#   2. package: 디렉토리 시작에서 끝까지
#   3. module: 파일 시작에서 끝까지
#   4. class: 클래스 시작에서 끝까지
#   5. function: 함수 시작에서 끝까지 (default)
#
# autouse가 True이면 테스트 함수에 명시적으로 할당하지 않아도 암시적으로 실행
#  CAUTION: 테스트 수행시, 해당 fixture가 보여야 함 (같은 파일 & conftest.py)
@pytest.fixture(scope="session", autouse=True)
def program():
    start_program()

    yield

    stop_program()


# fixture가 yield로 반환하면 테스트 정리 작업을 할 수 있다.
@pytest.fixture
def clear_storage():
    yield

    storage.clear()  # 테스트 완료 후, 호출됨


# fixture가 fixture를 파라미터로 받는다. fixture 사이의 의존성 관리
@pytest.fixture
def robots(clear_storage):
    _robots = [
        Robot(id_=id_, name=name)
        for id_, name in [(1, "A"), (2, "B"), (3, "C"), (4, "B")]
    ]
    for o in _robots:
        storage.add(o)

    return _robots


# fixture는 테스트 함수의 파라미터로 주입받을 수 있다.
def test_storage_add_failed(clear_storage):
    storage.add(Robot(id_=1, name="A"))

    with pytest.raises(DuplicateEntity):
        storage.add(Robot(id_=1, name="B"))


def test_robot_get_by_id(robots):
    robot = robots[0]
    robot_found = Robot.get_by_id(storage, id_=robot.id)

    assert robot_found.id == robot.id
    assert robot_found.name == robot_found.name


def test_robot_get_by_id_failed(robots):
    max_id = max(o.id for o in robots)
    with pytest.raises(NotFoundEntity):
        Robot.get_by_id(storage, id_=max_id + 1)


def test_robot_find_by_name(robots):
    robots_found = Robot.find_by_name(storage, name="B")

    assert [(o.id, o.name) for o in robots_found] == [(2, "B"), (4, "B")]


def test_mul():
    assert 3 * 4 == mul(3, 4)
