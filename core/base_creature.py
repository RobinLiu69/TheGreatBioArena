from abc import ABC, abstractmethod
from typing import Sequence
from core.base_parts import BasePart

class BaseCreature(ABC):

    @abstractmethod
    def init_parts(self) -> Sequence[BasePart]:
        pass

    @abstractmethod
    def get_color(self) -> tuple[int, int, int]:
        pass

    @abstractmethod
    def move_logic(self,  energy_ratio: float, note: list) -> tuple[int, float]:
        pass

    @abstractmethod
    def reproduce_logic(self, energy_ratio: float, note: list) -> Sequence[int]:
        pass
