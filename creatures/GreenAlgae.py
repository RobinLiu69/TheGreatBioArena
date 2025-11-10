import random
from core.base_creature import BaseCreature
from core.base_parts import *

class GreenAlgae(BaseCreature):    
    def init_parts(self) -> list[BasePart]:
        return [NucleusCellulae()] + [Folium() for _ in range(8)]  + [Lorica() for _ in range(8)]

    def get_color(self) -> tuple[int, int, int]:
        return (120, 255, 120)

    def move_logic(self, energy_ratio, note) -> tuple[int, int]:
        return 0, 0

    def reproduce_logic(self, energy_ratio, note) -> list[int]:
        if energy_ratio > 2:
            return [1, 1]
        return []