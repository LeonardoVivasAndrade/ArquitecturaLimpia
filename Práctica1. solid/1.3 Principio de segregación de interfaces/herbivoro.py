from abc import ABC, abstractmethod
from animal import Animal

class Herbivoro(Animal):
    @abstractmethod
    def pastar(self):
        pass