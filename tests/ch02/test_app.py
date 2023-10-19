import pytest

from app.entity import Robot
from app.exceptions import NotFoundEntity, DuplicateEntity
from app.storage import storage
from app.utils import start_program, stop_program, mul


@pytest.fixture(scope="session", autouse=True)
def program():
    start_program()

    yield

    stop_program()


@pytest.fixture
def clear_storage():
    yield

    storage.clear()


@pytest.fixture
def robots(clear_storage):
    _robots = [
        Robot(id_=id_, name=name)
        for id_, name in [(1, "A"), (2, "B"), (3, "C"), (4, "B")]
    ]
    for o in _robots:
        storage.add(o)

    return _robots


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
