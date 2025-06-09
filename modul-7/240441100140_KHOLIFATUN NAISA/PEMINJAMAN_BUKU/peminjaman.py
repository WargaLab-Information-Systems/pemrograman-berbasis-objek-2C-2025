from abc import ABC, abstractmethod

class Peminjaman(ABC):
    @abstractmethod
    def pinjaman(self):
        pass
    
    @abstractmethod
    def kembalikan(self):
        pass

