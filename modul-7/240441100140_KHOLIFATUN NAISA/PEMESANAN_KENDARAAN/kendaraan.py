from abc import ABC, abstractmethod

class Kendaraan(ABC):
    @abstractmethod
    def booking(self):
        pass

    @abstractmethod
    def biaya(self):
        pass

    @abstractmethod
    def asuransi(self):
        pass