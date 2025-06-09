from abc import ABC, abstractmethod

class ReservasiInterface(ABC):
    @abstractmethod
    def reservasi(self):
        pass
