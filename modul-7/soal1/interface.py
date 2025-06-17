from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def proses_pembayaran(self, jumlah: float):
        pass
