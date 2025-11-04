import random
import pygame

class BasePart:
    def __init__(self, energy, can_reproduce=False, volume=0, attack=0, defense=0, speed=0, cost=0, photosynthesis_rate=0):
        self.can_reproduce = can_reproduce
        self.volume = volume
        self.energy = energy
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.cost = cost
        self.photosynthesis_rate = photosynthesis_rate
    
    def update(self, color):
        pass
    
    def draw(self, surface):
        pass


class Lorica(BasePart):
    def __init__(self):
        super().__init__(energy=3, volume=1, defense=7, cost=0.02)


class Spiculum(BasePart):
    def __init__(self):
        super().__init__(energy=1, attack=2, cost=0.02)


class Folium(BasePart):
    def __init__(self):
        super().__init__(energy=5, volume=0.2, cost=0.01, photosynthesis_rate=0.07)


class NucleusCellulae(BasePart):
    def __init__(self):
        super().__init__(energy=3, can_reproduce=True, volume=0.5, defense=1,  cost=0.01)


class Cytoplasma(BasePart):
    def __init__(self):
        super().__init__(energy=1, volume=0.5, defense=2, speed=2, cost=0.01)


class CytoplasmaMobilis(BasePart):
    def __init__(self):
        super().__init__(energy=1, volume=0.5, speed=5, cost=0.02)

class CytoplasmaMagnum(BasePart):
        def __init__(self):
            super().__init__(energy=2, volume=3, defense=2, speed=1, cost=0.02)