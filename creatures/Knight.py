import random
from core.base_creature import BaseCreature
from core.base_parts import *

class Knight(BaseCreature):
    def init_parts(self) -> list[BasePart]:
        return [NucleusCellulae()] + [Lorica() for _ in range(3)] + [Spiculum() for _ in range(6)] + [Folium() for _ in range(4)] + [CytoplasmaMagnum()]

    def get_color(self) -> tuple[int, int, int]:
        return (148, 148, 73)

    def move_logic(self, energy_ratio, note) -> tuple[int, int]:
        if energy_ratio < 2:
            if len(note) == 1:
                note["方向"] = 45+(random.randint(0, 3)*90)
                note["速度"] = 1
            note["速度"] -= 0.002
            return note["方向"], note["速度"]
        else:
            if len(note) == 1 or note["方向"] ==360:
                note["方向"] = 0
            note["方向"] += 1
            return note["方向"], 0.2

    def reproduce_logic(self, energy_ratio, note) -> list[int]:
        if energy_ratio > 6:
            return [3, 1]
        return []