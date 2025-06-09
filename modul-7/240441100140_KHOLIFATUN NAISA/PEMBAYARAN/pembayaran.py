from abc import ABC, abstractmethod

class Pembayaran(ABC):
    @abstractmethod
    def bayar(self):
        pass
