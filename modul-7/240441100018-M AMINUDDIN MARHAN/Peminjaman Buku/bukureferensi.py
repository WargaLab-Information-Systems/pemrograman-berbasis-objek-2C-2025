from peminjaman import Peminjaman
from reservasi import Reservasi

class BukuReferensi(Peminjaman, Reservasi):
    def __init__(self, jumlah_buku):
        if not isinstance(jumlah_buku, int) or jumlah_buku <= 0:
            raise ValueError("Jumlah buku harus lebih dari 0")
        self.__jumlah_buku = jumlah_buku

    @property
    def jumlah_buku(self):
        return self.__jumlah_buku
    
    def pinjam(self):
        if self.__jumlah_buku > 3:
            return "Jumlah buku referensi yang dapat dipinjam maksimal 3 buku"
        return f"{self.__jumlah_buku} buku referensi berhasil dipinjam"
    
    def reservasi(self):
        return f"{self.__jumlah_buku} buku referensi berhasil diresevasi"