import random
from core.base_creature import BaseCreature
from core.base_parts import *

class Wowkfccc(BaseCreature):    
    def init_parts(self) -> list[BasePart]:
        return [NucleusCellulae()] + [Folium() for _ in range(6)] + [Spiculum() for _ in range(7)] + [Lorica() for _ in range(7)] + [Cytoplasma()] + [CytoplasmaMobilis() for _ in range(3)]
 
    def get_color(self) -> tuple[int, int, int]:
        return (30, 0, 255)

    def move_logic(self, energy_ratio, note) -> tuple[int, float]:
        d = [0, 30,60,90,120, 180,210,240, 270]
        note["速度"] = 0.8
        note["方向"] = 90
        note["方向"] = d[int(note["_time"]/9)%9]
        if note['速度'] > 0.5: 
            note["速度"] -= 0.1
            note["方向"] = d[int(note["_time"]/9)%9]
            return note["方向"], note["速度"] 
        if note['速度'] < 0.5: 
            note["速度"] += 0.1
            note["方向"] = d[int(note["_time"]/9)%9]
            return note["方向"], note["速度"] 
        return note["速度"], note["速度"]

    def reproduce_logic(self, energy_ratio, note) -> list[int]:
        if energy_ratio > 2:
            return [0.8, 0.1, 0.1]
        return []