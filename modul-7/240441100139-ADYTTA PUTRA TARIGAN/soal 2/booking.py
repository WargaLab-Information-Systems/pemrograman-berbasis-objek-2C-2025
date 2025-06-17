from abc import ABC, abstractmethod

class Booking(ABC):
    @abstractmethod
    def proses_booking(self, nama, usia):
        pass

    @abstractmethod
    def hitung_biaya(self):
        pass

    @abstractmethod
    def info_asuransi(self):
        pass
