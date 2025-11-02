import random
from core.base_creature import BaseCreature
from core.base_parts import BasePart, CellNucleus, Leaf, Spike, Cytoplasm, Armor

class LuckerCreature(BaseCreature):    
    def init_parts(self) -> list[BasePart]:
        return [CellNucleus()] + [Leaf() for _ in range(6)] + [Spike() for _ in range(7)] + [Armor() for _ in range(7)] + [Cytoplasm()]
 
    def get_color(self) -> tuple[int, int, int]:
        return (225, 255, 0)

    def move_logic(self, note) -> tuple[int, float]:
        return random.randint(0, 120), 0.1

    def reproduce_logic(self, energy_ratio, note) -> list[int]:
        if energy_ratio > random.randint(2, 6):
            return [random.random(), random.random()]
        return []
