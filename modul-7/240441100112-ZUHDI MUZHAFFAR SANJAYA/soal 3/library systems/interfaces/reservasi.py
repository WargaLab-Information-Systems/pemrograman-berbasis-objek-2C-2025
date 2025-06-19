from abc import ABC, abstractmethod

class Reservasi(ABC):
    @abstractmethod
    def reservasi(self):
        pass

    @abstractmethod
    def batalkan_reservasi(self):
        pass