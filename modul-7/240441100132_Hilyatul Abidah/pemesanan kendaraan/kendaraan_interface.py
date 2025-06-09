from abc import ABC, abstractmethod

class KendaraanInterface(ABC):
    @abstractmethod
    def validasi_usia(self, usia: int) -> bool:
        pass

    @abstractmethod
    def proses_booking(self):
        pass

    @abstractmethod
    def hitung_biaya(self) -> int:
        pass

    @abstractmethod
    def info_asuransi(self):
        pass
