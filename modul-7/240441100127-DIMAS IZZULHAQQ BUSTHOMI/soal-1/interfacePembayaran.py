from abc import ABC, abstractmethod

class Pembayaran(ABC):
    @abstractmethod
    def prosesPembayaran(self, jumlah):
        pass