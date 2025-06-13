from abc import ABC, abstractmethod
class SistemPembayaran(ABC):
    @abstractmethod
    def __init__(self, jumlah):
        pass
    @abstractmethod
    def bayar(self):
        pass