import random
from core.base_creature import BaseCreature
from core.base_parts import *

class Grass(BaseCreature):    
    def init_parts(self) -> list[BasePart]:
        return [NucleusCellulae()] + [Folium() for _ in range(5)] + [CytoplasmaMobilis()]

    def get_color(self) -> tuple[int, int, int]:
        return (120, 255, 120)

    def move_logic(self, energy_ratio, note) -> tuple[int, int]:
        if len(note) == 0:
            note.append(random.randint(0, 360))
            note.append(1)
        note[1] -= 0.02
        return note[0], note[1]

    def reproduce_logic(self, energy_ratio, note) -> list[int]:
        if energy_ratio > 1:
            return [1, 1, 1, 1]
        return []
