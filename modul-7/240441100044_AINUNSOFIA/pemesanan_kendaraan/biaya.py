from abc import ABC, abstractmethod

class Biaya(ABC):
    @abstractmethod
    def hitung_biaya(self, durasi: int) -> float:
        pass