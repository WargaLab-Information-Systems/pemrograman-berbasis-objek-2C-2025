from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def proses_pembayaran(self, jumlah: float) -> float:
        pass