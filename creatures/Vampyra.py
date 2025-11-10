import random
from core.base_creature import BaseCreature
from core.base_parts import *

class Vampyra(BaseCreature):
    '''
    The winner made by Robin
    '''
    def init_parts(self) -> list[BasePart]:
        return [
            NucleusCellulae(),
            Cytoplasma()] + [Spiculum() for _ in range(11)] + [Lorica() for _ in range(7)] + [Folium() for _ in range(4)]

    def get_color(self) -> tuple[int, int, int]:
        return (180, 0, 220)

    def move_logic(self, energy_ratio, note) -> tuple[int, float]:
        if len(note) == 1:
            note["dir"] = random.randint(0, 360)
            note["speed"] = 0.5
        if note["_time"]%5 < 0.1 and note["_time"] > 1:
            note["dir"] = random.randint(0, 360)
            note["_time"] = 0
            note["speed"] = 1
        return note["dir"], note["speed"]

    def reproduce_logic(self, energy_ratio, note) -> list[int]:
        if energy_ratio > 4:
            return [2, 1]
        return []