import random
from core.base_creature import BaseCreature
from core.base_parts import *

class Killer(BaseCreature):
    def init_parts(self) -> list[BasePart]:
        return [NucleusCellulae(), Lorica()] + [Spiculum() for _ in range(6)] + [Folium(), Cytoplasma()]

    def get_color(self) -> tuple[int, int, int]:
        return (255, 25, 25)

    def move_logic(self, energy_ratio, note) -> tuple[int, int]:
        if len(note) == 0:
            note["方向"] = random.randint(0, 360)
            note["時間"] = 0
        elif note["時間"]==20:
            note["時間"] = 0
            note["方向"] = random.randint(0, 360)
        else:
            note["時間"] +=1
        return note["方向"], 0.2

    def reproduce_logic(self, energy_ratio, note) -> list[int]:
        if energy_ratio > 5:
            return [4, 1]
        return []
