import pygame, importlib, os, math
from core.base_entity import BioEntity
from core.base_creature import BaseCreature

class World:
    def __init__(self, screen: pygame.surface.Surface):
        self.entities: list[BioEntity] = []
        self.screen = screen
        self.win = False
        self.width, self.height = screen.get_size()
        self.load_creatures()

    def load_creatures(self):
        path = "creatures"
        for file_name in os.listdir(path):
            if file_name.endswith(".py"):
                module_name = f"{path}.{file_name[:-3]}"
                module = importlib.import_module(module_name)
                
                for attr in dir(module):
                    obj = getattr(module, attr)
                    if isinstance(obj, type) and issubclass(obj, BaseCreature) and obj is not BaseCreature:
                        creature_base_energy = sum(part.energy for part in obj().init_parts())
                        if creature_base_energy > 100: break
                        number_of_creatures = (100//sum(part.energy for part in obj().init_parts()))
                        print(attr, creature_base_energy, number_of_creatures)
                        creature_energy = round(int(100/number_of_creatures), 3)
                        print(creature_energy)
                        for i in range(number_of_creatures):
                            creature = obj()
                            entity = BioEntity(attr, creature, self.width, self.height, creature_energy)
                            self.entities.append(entity)
    
    def update(self, dt: float):
        new_entities = []
        name_energy = {}
        for entity in self.entities:
            spawn = entity.update(dt, self.entities)
            new_entities.extend(spawn)
        self.entities = [entity for entity in self.entities if entity.alive]

        self.entities.extend(new_entities)

        creature_names = set([entity.name for entity in self.entities if entity.alive])
        world_total_energy = sum(entity.energy for entity in self.entities)
        for name in creature_names:
            name_energy[name] = round(sum([entity.energy for entity in self.entities if entity.name == name]))
            if name_energy[name]/world_total_energy > 0.95:
                pass

        if not self.win:
            print(f"\r{name_energy}".ljust(80), end="", flush=True)

    def draw(self):
        self.screen.fill((50, 100, 255))
        for entity in self.entities:
            pygame.draw.circle(self.screen, entity.color, (int(entity.x), int(entity.y)), int(entity.size))