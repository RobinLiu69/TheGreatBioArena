import random
from core.base_creature import BaseCreature
from core.base_parts import *

class GrassPlus(BaseCreature):    
    def init_parts(self) -> list[BasePart]:
        return [NucleusCellulae(), Spiculum()] + [Folium() for _ in range(8)] + [CytoplasmaMobilis()]

    def get_color(self) -> tuple[int, int, int]:
        return (120, 255, 120)

    def move_logic(self, energy_ratio, note) -> tuple[int, int]:
        if "速度" not in note:
            note["方向"] = random.randint(0, 360)
            note["速度"] = 1
        note["速度"] -= 0.002
        return note["方向"], note["速度"]

    def reproduce_logic(self, energy_ratio, note) -> list[int]:
        if energy_ratio > 0.5:
            return [1, 1, 1, 1]
        return []