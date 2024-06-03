from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def respirar(self):
        pass
    
    @abstractmethod
    def comer(self):
        pass
    
    @abstractmethod
    def dormir(self):
        pass