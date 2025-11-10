import math, random
from core import base_parts as bp
from core import base_creature

def random_position(width=1200, height=800):
    return random.randint(50, width - 50), random.randint(50, height - 50)


class BioEntity:
    def __init__(self, name, module: base_creature.BaseCreature, width, height, energy):
        self.name = name
        self.module = module
        self.note = {"_time": 0.0}
        self.parts = module.init_parts()
        self.len_of_parts = len(self.parts)
        self.year_old = 0

        self.base_energy = sum(part.energy for part in self.parts)
        self.base_vol = 10 + sum(getattr(part, "volume", 0) for part in self.parts)
        self.photosynthesis_rate = sum(getattr(part, "photosynthesis_rate", 0) for part in self.parts)
        self.base_def = sum(getattr(part, "defense", 0) for part in self.parts)
        self.base_atk = sum(getattr(part, "attack", 0) for part in self.parts)
        self.base_spd = sum(getattr(part, "speed", 0) for part in self.parts)
        self.cost = sum(getattr(part, "cost", 0) for part in self.parts)

        self.energy = energy
        self.energy_ratio = self.energy / self.base_energy
        self.volume = self.base_vol
        self.defense = self.base_def * self.energy_ratio
        self.max_defense = self.base_def * self.energy_ratio
        self.attack = self.base_atk * self.energy_ratio
        self.speed = self.base_spd * self.energy_ratio

        self.color = self.module.get_color()
        self.x, self.y = random_position(width, height)
        self.vx = self.vy = 0
        self.size = self.volume * self.energy_ratio
        self.alive = True
        self.width = width
        self.height = height

    def update(self, dt: float, entities: list["BioEntity"]) -> list["BioEntity"]:
        if not self.alive:
            return []

        self.note["_time"] += dt
        
        direction, speed_ratio = self.module.move_logic(self.energy_ratio, self.note)
        if direction is not None:
            self.move(direction, speed_ratio, dt)
        
        world_total_energy = sum((entity.energy for entity in entities))


        self.comsume_energy(self.cost * dt * self.energy_ratio * max(1, (2 ** (self.len_of_parts-24))))
        self.comsume_energy(self.speed * dt * speed_ratio / 100)
        self.gain_energy(self.photosynthesis_rate * dt * self.energy_ratio * 8 / (2**max(0, int(math.log2(world_total_energy))-7)))

        if self.energy < 1:
            self.alive = False
            return []
        
        self.energy = min(250, self.energy)

        self.energy_ratio = self.energy/self.base_energy
        self.size = self.volume * self.energy_ratio
        self.attack = self.base_atk * self.energy_ratio
        self.speed = self.base_spd * self.energy_ratio
        self.max_defense = self.base_def * self.energy_ratio


        if self.defense < self.max_defense:
            self.defense += 0.1 * dt * 60
            if self.defense > self.max_defense:
                self.defense = self.max_defense

        self.boundary_check()


        ratios = self.module.reproduce_logic(self.energy_ratio, self.note)
        if ratios and self.parts[0].can_reproduce:
            self.alive = False
            return self.reproduce(ratios)
        
        self.handle_collisions(dt, entities)

        return []

    def move(self, direction: int, speed_ratio: float, dt: float):
        rad = math.radians(direction%360)
        if not 0 < speed_ratio <= 1:
            return

        self.vx = math.cos(rad) * self.speed * speed_ratio
        self.vy = math.sin(rad) * self.speed * speed_ratio
        self.x += self.vx * dt * 60
        self.y += self.vy * dt * 60

    def boundary_check(self):
        if self.x < self.size:
            self.x = self.size
            self.vx = 0
        if self.x > self.width - self.size:
            self.x = self.width - self.size
            self.vx = 0
        if self.y < self.size:
            self.y = self.size
            self.vy = 0
        if self.y > self.height - self.size:
            self.y = self.height - self.size
            self.vy = 0

    def comsume_energy(self, comsume: float) -> None:
        self.energy -= comsume

    def gain_energy(self, gain: float) -> None:
        self.energy += gain * random.randint(90, 100)/100

    def handle_collisions(self, dt: float, entities: list["BioEntity"]) -> None:
        for other in entities:
            if not self.alive:
                break
            if other is self or not other.alive:
                continue
            dx = self.x - other.x
            dy = self.y - other.y
            dist = math.hypot(dx, dy)
            if dist < (self.size + other.size):
                other.defense -= self.attack
                self.energy -= self.attack/10
                self.defense -= other.attack
                other.energy -= other.attack/10

                if self.defense <= 0 and other.defense <= 0:
                    temp = [self, other]
                    lost = random.randint(0, 1)
                    temp[lost].alive = False
                    temp[not lost].energy += temp[lost].energy
                elif other.defense <= 0:
                    other.alive = False
                    self.energy += other.energy
                elif self.defense <= 0:
                    self.alive = False
                    other.energy += self.energy
                    
                angle = math.atan2(dy, dx)
                push = (self.size + other.size - dist) / 2
                self.x += math.cos(angle) * push
                self.y += math.sin(angle) * push
                other.x -= math.cos(angle) * push
                other.y -= math.sin(angle) * push


    def reproduce(self, ratios) -> list["BioEntity"]:
        ratios = tuple(map(abs, ratios))
        total = sum(ratios)
        children: list[BioEntity] = []
        for ratio in ratios:
            child_energy = self.energy * (ratio / total) * 0.9
            child = BioEntity(self.name, self.module, self.width, self.height, energy=child_energy)
            child.x = self.x + random.randint(-int(self.size*1), int(self.size*1))
            child.y = self.y + random.randint(-int(self.size*1), int(self.size*1))
            children.append(child)

        return children

