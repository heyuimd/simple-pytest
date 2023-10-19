import pytest

from app.entity import Robot
from app.exceptions import NotFoundEntity
from app.storage import storage


# module 안에서 사용할 fixture는 파일 안에 정의하자: 관련있는 로직을 가까이 유지해야 코드 읽기 편하다.
@pytest.fixture
def robots(clear_storage):
    _robots = [
        Robot(id_=id_, name=name)
        for id_, name in [(1, "A"), (2, "B"), (3, "C"), (4, "B")]
    ]
    for o in _robots:
        storage.add(o)

    return _robots


def test_get_by_id(robots):
    robot = robots[0]
    robot_found = Robot.get_by_id(storage, id_=robot.id)

    assert robot_found.id == robot.id
    assert robot_found.name == robot_found.name


def test_get_by_id_failed(robots):
    max_id = max(o.id for o in robots)
    with pytest.raises(NotFoundEntity):
        Robot.get_by_id(storage, id_=max_id + 1)


def test_find_by_name(robots):
    robots_found = Robot.find_by_name(storage, name="B")

    # then
    assert [(o.id, o.name) for o in robots_found] == [(2, "B"), (4, "B")]
