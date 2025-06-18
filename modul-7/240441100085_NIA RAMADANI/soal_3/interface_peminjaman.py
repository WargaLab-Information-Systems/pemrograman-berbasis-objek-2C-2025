from abc import ABC, abstractmethod

class Peminjaman(ABC):
    @abstractmethod
    def pinjam(self, buku):
        pass

class SistemPeminjaman(Peminjaman):
    def pinjam(self, buku):
        if buku.tipe_buku() == "Referensi":
            return f"Buku '{buku.judul}' adalah buku referensi dan tidak bisa dipinjam."
        else:
            return f"Buku '{buku.judul}' berhasil dipinjam."
