from peminjaman import Peminjaman
from reservasi import Reservasi

class BukuFiksi(Peminjaman, Reservasi):
    def __init__(self, jumlah_buku):
        if not isinstance(jumlah_buku, int) or jumlah_buku <= 0:
            raise ValueError("Jumlah buku harus lebih dari 0")
        self.__jumlah_buku = jumlah_buku

    @property
    def jumlah_buku(self):
        return self.__jumlah_buku
    
    def pinjam(self):
        if self.__jumlah_buku > 5:
            return "Jumlah buku fiksi yang dapat dipinjam maksimal 5 buku"
        return f"{self.__jumlah_buku} buku fiksi berhasil dipinjam"
    
    def reservasi(self):
        return f"{self.__jumlah_buku} buku fiksi berhasil diresevasi"