import random
from core.base_creature import BaseCreature
from core.base_parts import *

class Spora(BaseCreature):    
    def init_parts(self) -> list[BasePart]:
        return [NucleusCellulae()] + [Folium() for _ in range(19)] + [CytoplasmaMobilis() for _ in range(2)]

    def get_color(self) -> tuple[int, int, int]:
        return (120, 100, 0)

    def move_logic(self, energy_ratio, note) -> tuple[int, int]:
        if "speed" not in note:
            note["dir"] = random.choice([0, 90, 160, 270])
            note["speed"] = 1
            note["time"] = 0
            note["moved"] = False
        elif note["time"] == 1 and not note["moved"]:
            note["dir"] = random.choice([0, 90, 160, 270])
            note["speed"] = 1
            note["moved"] = True
        
        if note["_time"] > 10:
            if note["speed"] > 0:
                note["time"] = 1
    
        return note["dir"], note["speed"]

    def reproduce_logic(self, energy_ratio, note) -> list[int]:
        if energy_ratio > 0.1:
            return [1, 1, 1, 1]
        return []