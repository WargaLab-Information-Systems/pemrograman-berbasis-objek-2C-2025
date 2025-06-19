from abc import ABC, abstractmethod

class BookingInterface(ABC):
    @abstractmethod
    def proses_booking(self, user):
        pass

    @abstractmethod
    def hitung_biaya(self):
        pass

    @abstractmethod
    def asuransi(self):
        pass