import random
from core.base_creature import BaseCreature
from core.base_parts import *

class ExampleCreature(BaseCreature):
    def init_parts(self) -> list[BasePart]:
        return [CellNucleus(),Armor(), Armor(), Spike(), Spike(), Spike(), Spike(), Leaf(),Leaf(),Leaf(),Leaf(),Leaf(),Leaf(),Leaf(),Leaf(), Cytoplasm()]

    def get_color(self) -> tuple[int, int, int]:
        return (148, 148, 73)

    def move_logic(self, note) -> tuple[int, int]:
        return 0, 0

    def reproduce_logic(self, energy_ratio, note) -> list[int]:
        if energy_ratio > 5:
            return [1, 1]
        return []