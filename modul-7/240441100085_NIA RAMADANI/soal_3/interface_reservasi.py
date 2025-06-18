from abc import ABC, abstractmethod

class Reservasi(ABC):
    @abstractmethod
    def reservasi(self, buku):
        pass

class SistemReservasi(Reservasi):
    def reservasi(self, buku):
        return f"Buku '{buku.judul}' berhasil direservasi."
