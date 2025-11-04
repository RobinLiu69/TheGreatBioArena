import pygame, importlib, os, math
from core.base_entity import BioEntity
from core.base_creature import BaseCreature

class World:
    def __init__(self, screen: pygame.surface.Surface):
        self.entities: list[BioEntity] = []
        self.screen = screen
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
                        for i in range(math.ceil(100/sum(part.energy for part in obj().init_parts()))):
                            creature = obj()
                            entity = BioEntity(attr, creature, self.width, self.height)
                            self.entities.append(entity)
    
    def update(self, dt: float):
        new_entities = []
        for entity in self.entities:
            spawn = entity.update(dt, self.entities)
            new_entities.extend(spawn)
        self.entities = [entity for entity in self.entities if entity.alive]

        print(sum([entity.energy for entity in self.entities if entity.alive]))
        
        self.entities.extend(new_entities)

    def draw(self):
        self.screen.fill((50, 100, 255))
        for entity in self.entities:
            pygame.draw.circle(self.screen, entity.color, (int(entity.x), int(entity.y)), int(entity.size))
