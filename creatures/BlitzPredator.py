import random
from core.base_creature import BaseCreature
from core.base_parts import *

class BlitzPredator(BaseCreature):


    def init_parts(self) -> list[BasePart]:
        return [
            NucleusCellulae(),
            Lorica(), Lorica(), Lorica(), Lorica(), Lorica(), Lorica(), Lorica(),  Lorica(), Lorica(), Lorica(), 
            Spiculum(), Spiculum(),
            Folium(), Folium(), Folium(), Folium(), Folium(), Folium(), 
            Cytoplasma(), 
        ]

    def get_color(self) -> tuple[int, int, int]:
        return (0, 0, 0)

    def move_logic(self, energy_ratio: float, note: dict) -> tuple[int, float]:

        if "angle" not in note:
            if energy_ratio < 0.5:
                note["angle"] = random.choice([45, 135, 225, 315])  # 四角
            else:
                note["angle"] = random.choice([i * 22.5 for i in range(16)])  # 16方向
            note["next_turn"] = random.uniform(180, 360)

        t = note["_time"]

        if t >= note.get("next_turn", 0):
            if energy_ratio < 0.5:
                note["angle"] = random.choice([45, 135, 225, 315])
            else:
                note["angle"] = random.choice([i * 22.5 for i in range(16)])
            note["next_turn"] = t + random.uniform(180, 360)


        if energy_ratio < 0.5:
            speed = 0.5
        elif energy_ratio < 3.0:
            speed = 0.3
        else:
            speed = 0.4

        return int(note["angle"]), float(speed)

    def reproduce_logic(self, energy_ratio: float, note: dict) -> list[int]:

        if energy_ratio > 1.51:
            return [10, 1]
        elif energy_ratio > 12:
            return [1,1]
        elif energy_ratio > 2.2:
            return [100, 1]
        elif note["_time"] > 600:
            return [1, 1]
        return [] 