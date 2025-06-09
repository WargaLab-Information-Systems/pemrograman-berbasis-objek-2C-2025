from abc import ABC, abstractmethod

class Booking(ABC):
    @abstractmethod
    def proses_booking(self, nama, usia):
        pass

    @abstractmethod
    def biaya(self):
        pass

    @abstractmethod
    def asuransi(self):
        pass