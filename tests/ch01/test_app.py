from unittest import TestCase

from app.entity import Robot
from app.exceptions import NotFoundEntity, DuplicateEntity
from app.storage import storage
from app.utils import start_program, stop_program, mul


def get_robots() -> list[Robot]:
    return [
        Robot(id_=id_, name=name)
        for id_, name in [(1, "A"), (2, "B"), (3, "C"), (4, "B")]
    ]


class AppTest(TestCase):
    @classmethod
    def setUpClass(cls):
        start_program()

    @classmethod
    def tearDownClass(cls):
        stop_program()

    def tearDown(self):
        storage.clear()

    def test_storage_add_failed(self):
        # given
        storage.add(Robot(id_=1, name="A"))

        # when / then
        with self.assertRaises(DuplicateEntity):
            storage.add(Robot(id_=1, name="B"))

    def test_robot_get_by_id(self):
        # given
        robots = get_robots()
        for o in robots:
            storage.add(o)

        # when
        robot = robots[0]
        robot_found = Robot.get_by_id(storage, id_=robot.id)

        # then
        self.assertEqual(robot_found.id, robot.id)
        self.assertEqual(robot_found.name, robot.name)

    def test_robot_get_by_id_failed(self):
        # given
        robots = get_robots()
        for o in robots:
            storage.add(o)

        # when / then
        max_id = max(o.id for o in robots)
        with self.assertRaises(NotFoundEntity):
            Robot.get_by_id(storage, id_=max_id + 1)

    def test_robot_find_by_name(self):
        # given
        robots = get_robots()
        for o in robots:
            storage.add(o)

        # when
        robots_found = Robot.find_by_name(storage, name="B")

        # then
        self.assertEqual([(o.id, o.name) for o in robots_found], [(2, "B"), (4, "B")])

    def test_mul(self):
        self.assertEqual(3 * 4, mul(3, 4))
