from abc import ABC, abstractmethod
from typing import Any


class Storage(ABC):
    @abstractmethod
    def add(self, obj: Any):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def get_by_id(self, id_: int) -> Any:
        pass

    @abstractmethod
    def find(self, key: str, value: Any) -> Any:
        pass


class Entity(ABC):
    @abstractmethod
    def get_id(self) -> int:
        pass
