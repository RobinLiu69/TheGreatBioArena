import random
from core.base_creature import BaseCreature
from core.base_parts import *

class ExampleCreature(BaseCreature):
    def init_parts(self) -> list[BasePart]:
        return [CellNucleus(), Armor(), Spike(), Spike(), Spike(), Spike(), Spike(), Spike(), Leaf(), Cytoplasm()]

    def get_color(self) -> tuple[int, int, int]:
        return (255, 25, 25)

    def move_logic(self, energy_ratio, note) -> tuple[int, int]:
        if len(note) == 0:
            note.append(random.randint(0, 360))
            note.append(0)
        elif note[1]==20:
            note[1] = 0
            note[0] = random.randint(0, 360)
        else:
            note[1] +=1
        return note[0], 0.2

    def reproduce_logic(self, energy_ratio, note) -> list[int]:
        if energy_ratio > 5:
            return [4, 1]
        return []