import random
from core.base_creature import BaseCreature
from core.base_parts import *

class Shadow(BaseCreature):

    def init_parts(self) -> list[BasePart]:
        return [NucleusCellulae()] + \
               [Folium() for _ in range(8)] + \
               [Spiculum() for _ in range(18)] + \
               [Lorica() for _ in range(5)] + \
               [CytoplasmaMobilis() for _ in range(5)]
 
    def get_color(self) -> tuple[int, int, int]:
        return (252, 230, 201)

    # 實現高速左右來回移動邏輯
    def move_logic(self, energy_ratio, note) -> tuple[int, float]:
        # 1. 初始化方向和計時器
        if "direction" not in note:

            note["direction"] = 90

            note["dir_timer"] = 0.0



        current_time = note["_time"]


        if current_time - note["dir_timer"] >= 2.0:

            current_dir = note["direction"]
            if current_dir == 90:

                note["direction"] = 270
            else:

                note["direction"] = 90


            note["dir_timer"] = current_time


        direction = note["direction"]
        speed_ratio = 1.0

        return direction, speed_ratio

    def reproduce_logic(self, energy_ratio, note) -> list[float]:

        return []