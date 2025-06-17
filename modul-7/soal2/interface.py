from abc import ABC, abstractmethod

class BookingInterface(ABC):
    @abstractmethod
    def proses_booking(self, nama, usia):
        pass

    @abstractmethod
    def hitung_biaya(self) :
        pass

    @abstractmethod
    def informasi_asuransi(self):
        pass
