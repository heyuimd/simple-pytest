from typing import Any

from app.exceptions import DuplicateEntity, NotFoundEntity
from app.lib import Storage, Entity


class MemoryStorage(Storage):
    __storage: dict[int, Entity] = dict()

    def add(self, obj: Entity):
        if self.__storage.get(obj.get_id()):
            raise DuplicateEntity

        self.__storage[obj.get_id()] = obj

    def clear(self):
        self.__storage.clear()

    def get_by_id(self, id_: int) -> Any:
        if obj := self.__storage.get(id_):
            return obj

        raise NotFoundEntity

    def find(self, key: str, value: int | str) -> list[Entity]:
        objs = []

        for o in self.__storage.values():
            if not hasattr(o, key):
                continue

            if getattr(o, key) == value:
                objs.append(o)

        return objs


storage = MemoryStorage()
