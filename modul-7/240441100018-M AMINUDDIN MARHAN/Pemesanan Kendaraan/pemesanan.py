from abc import ABC, abstractmethod
class PemesananKendaraan(ABC):
    @abstractmethod
    def __init__(self, usia):
        pass

    @abstractmethod
    def booking(self):
        pass

    @abstractmethod
    def biaya(self):
        pass

    @abstractmethod
    def asuransi(self):
        pass