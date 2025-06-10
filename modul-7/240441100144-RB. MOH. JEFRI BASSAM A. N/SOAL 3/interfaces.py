from abc import ABC, abstractmethod

class Peminjaman(ABC):
    @abstractmethod
    def info_buku(self):
        pass
    @abstractmethod
    def hitung_denda(self, lama_pinjam):
        pass