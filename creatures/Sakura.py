import random
from core.base_creature import BaseCreature
from core.base_parts import *

class Sakura(BaseCreature):    
    def init_parts(self) -> list[BasePart]:
        return [NucleusCellulae()] + [Folium() for _ in range(5)] + [CytoplasmaMobilis()]
    def get_color(self) -> tuple[int, int, int]:
        return (225, 188, 225)

    def move_logic(self, energy_ratio, note) -> tuple[int, float]:
        if len(note) == 1:
            note["方向"] = random.randint(0, 360)
            note["速度"] = 1
            note["timer"] = 0.0

        dt = 1 / 20  
        note["timer"] += dt

        decay_time = max(0.01, 3.0)  # 安全值，防止為 0
        decay_rate = 1.0 / decay_time  

        note["速度"] -= decay_rate * dt  
        note["速度"] = max(0.0, note["速度"]) 

        return note["方向"], note["速度"]

    def reproduce_logic(self, energy_ratio, note) -> list[int]:
        if energy_ratio > 0.5 :
            return [1, 1, 1, 1, 1, 1, 1, 1]
        return []