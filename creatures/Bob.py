import random
from core.base_creature import BaseCreature
from core.base_parts import *

class Bob(BaseCreature):
    def init_parts(self) -> list[BasePart]:
        return [NucleusCellulae()] + [Lorica() for _ in range(15)] + [Spiculum() for _ in range(2)] + \
               [Folium() for _ in range(1)] + [Cytoplasma() for _ in range(4)] + [CytoplasmaMobilis()]

    def get_color(self) -> tuple[int, int, int]:
        return (255, 255, 255) 

    def calc_dir(self, note):
        if(note["_time"]//0.5%4==0):
            return random.randint(0, 90)
        elif(note["_time"]//0.5%4==1):
            return random.randint(270-60, 270+60)
        elif(note["_time"]//0.5%4==2):
            return random.randint(90, 180)
        elif(note["_time"]//0.5%4==3):
            return random.randint(270-60, 270+60)

    def move_logic(self, energy_ratio, note) -> tuple[int, float]:
        if energy_ratio > 1.5:
            return self.calc_dir(note), 0.9
        elif energy_ratio > 1:
            return self.calc_dir(note), 0.5
        else:
            return self.calc_dir(note), 0.2

    def reproduce_logic(self, energy_ratio, note) -> list[int]:
        if energy_ratio > 3:
            return [1, 0.01]
        return []