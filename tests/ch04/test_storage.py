import pytest

from app.entity import Robot
from app.exceptions import DuplicateEntity
from app.storage import storage


def test_add_failed(clear_storage):
    storage.add(Robot(id_=1, name="A"))

    with pytest.raises(DuplicateEntity):
        storage.add(Robot(id_=1, name="B"))
