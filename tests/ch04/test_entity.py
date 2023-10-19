import pytest

from app.entity import Robot
from app.exceptions import NotFoundEntity
from app.storage import storage


@pytest.fixture
def robots(request, clear_storage):
    params = getattr(request, "param", [(1, "A"), (2, "B")])
    _robots = [Robot(id_=id_, name=name) for id_, name in params]
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


@pytest.mark.parametrize(
    "robots, name, expecting",
    [
        (
            [(1, "A"), (2, "B"), (3, "C"), (4, "B")],
            "B",
            [(2, "B"), (4, "B")],
        ),
        (
            [(1, "A"), (2, "B"), (3, "C")],
            "C",
            [(3, "C")],
        ),
        # 없으면 빈 배열 반환
        (
            [(1, "A"), (2, "B"), (3, "C"), (4, "B")],
            "AA",
            [],
        ),
    ],
    indirect=["robots"],
)
def test_find_by_name(robots, name, expecting):
    robots_found = Robot.find_by_name(storage, name=name)

    # then
    assert [(o.id, o.name) for o in robots_found] == expecting
