import random
from core.base_creature import BaseCreature
from core.base_parts import *

class Berry(BaseCreature):    
    def init_parts(self) -> list[BasePart]:
        
        return [NucleusCellulae()] + [Folium() for _ in range(6)] + [Spiculum() for _ in range(7)] + [Lorica() for _ in range(7)] + [Cytoplasma() for _ in range(3)] + [CytoplasmaMobilis() for _ in range(1)]
    def get_color(self) -> tuple[int, int, int]:
        return (0x6F, 0x00, 0xD2)

    def move_logic(self, energy_ratio, note) -> tuple[int, float]:
        # directions = [0, 90, 180, 270]
        # return directions[int(note["_time"]/4)%4], 0.75
        if "count" not in note:
            note["count"] = 1
        note["count"] = (note["count"] + 0.001)
        if note["count"] > 2:
            note["count"] = 0.001
        # print(note["count"])
        return int(note["_time"]*200*note["count"])%360, 0.75
    def reproduce_logic(self, energy_ratio, note) -> list[int]:
        # print(energy_ratio)
        if energy_ratio > 3.5:
            return [0.9, 0.1]
        return []