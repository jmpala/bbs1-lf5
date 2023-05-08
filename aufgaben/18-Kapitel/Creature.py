from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, hp: int, name: str, size: int, gold: int) -> None:
        self._hp = hp
        self._name = name
        self._size = size
        self._gold = gold

    @property
    def hp(self) -> int:
        return self._hp

    @hp.setter
    def hp(self, value: int) -> None:
        self._hp = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, value: int) -> None:
        self._size = value

    @property
    def gold(self) -> int:
        return self._gold

    @gold.setter
    def gold(self, value: int) -> None:
        self._gold = value

    @abstractmethod
    def roll_dice(self, max_roll: int) -> int:
        pass

    @abstractmethod
    def hit_first(self) -> None:
        pass
