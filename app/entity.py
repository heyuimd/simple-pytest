from app.lib import Entity, Storage


class Robot(Entity):
    """storage에 저장할 robot entity"""

    id: int
    name: str

    def __init__(self, id_: int, name: str):
        self.id = id_
        self.name = name

    def get_id(self) -> int:
        return self.id

    @staticmethod
    def get_by_id(storage: Storage, id_: int) -> "Robot":
        return storage.get_by_id(id_)

    @staticmethod
    def find_by_name(storage: Storage, name: str) -> list["Robot"]:
        return storage.find("name", name)
