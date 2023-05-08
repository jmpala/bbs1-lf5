import random

from Creature import Creature


class Warrior(Creature):
    def __init__(self, hp: int, name: str, size: int, gold: int) -> None:
        super().__init__(hp, name, size, gold)

    def roll_dice(self, max_roll: int) -> int:
        return random.Random().randint(1, max_roll)

    def hit_first(self) -> None:
        print("Warrior hits first with 1D4")
        print("Warrior hits for", self.roll_dice(4), "damage")
