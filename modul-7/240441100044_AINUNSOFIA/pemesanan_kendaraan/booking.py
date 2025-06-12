from abc import ABC, abstractmethod

class Booking(ABC):
    @abstractmethod
    def proses_booking(self, nama: str, usia: int):
        pass
