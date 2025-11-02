from abc import ABC, abstractmethod
from core.base_parts import BasePart

class BaseCreature(ABC):

    @abstractmethod
    def init_parts(self) -> list[BasePart]:
        pass

    @abstractmethod
    def get_color(self) -> tuple[int, int, int]:
        pass

    @abstractmethod
    def move_logic(self, note: list) -> tuple[int, float]:
        pass

    @abstractmethod
    def reproduce_logic(self, energy_ratio: int, note: list) -> list[int]:
        pass
