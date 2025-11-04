import random
from core.base_creature import BaseCreature
from core.base_parts import *

class Knight(BaseCreature):
    def init_parts(self) -> list[BasePart]:
        return [NucleusCellulae()] + [Lorica() for _ in range(2)] + [Spiculum() for _ in range(4)] + [Folium() for _ in range(8)] + [Cytoplasma()]

    def get_color(self) -> tuple[int, int, int]:
        return (148, 148, 73)

    def move_logic(self, energy_ratio, note) -> tuple[int, int]:
        return 0, 0

    def reproduce_logic(self, energy_ratio, note) -> list[int]:
        if energy_ratio > 4.3:
            return [3, 1]
        return []