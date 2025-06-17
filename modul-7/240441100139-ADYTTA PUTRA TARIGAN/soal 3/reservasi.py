from abc import ABC, abstractmethod

class Reservasi(ABC):
    @abstractmethod
    def reservasi(self):
        pass

    @abstractmethod
    def batal_reservasi(self):
        pass