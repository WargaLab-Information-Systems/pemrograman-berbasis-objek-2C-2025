from abc import ABC, abstractmethod

class Peminjaman(ABC):
    @abstractmethod
    def pinjam(self):
        pass

    @abstractmethod
    def kembalikan(self):
        pass