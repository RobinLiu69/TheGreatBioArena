import random
from core.base_creature import BaseCreature
from core.base_parts import *

class CancerCell(BaseCreature):
    def init_parts(self) -> list[BasePart]:
        return [NucleusCellulae()] + [Spiculum() for _ in range(11)] + [Lorica() for _ in range(8)] + [Folium() for _ in range(4)]

    def get_color(self) -> tuple[int, int, int]:
        return (50, 50, 50)

    def move_logic(self, energy_ratio , note) -> tuple[int, float]:
        return 0, 0

    def reproduce_logic(self, energy_ratio: float, note: list) -> list[float]:
        if energy_ratio >= 0.1:
            return [0.1, 0.9]
        return []