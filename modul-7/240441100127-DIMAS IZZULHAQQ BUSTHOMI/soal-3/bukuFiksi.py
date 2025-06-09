from peminjamanInterface import Peminjaman
from reservasiInterface import Reservasi

class BukuFiksi(Peminjaman, Reservasi):
    def __init__(self, judul):
        self.__judul = judul

    @property
    def judul(self):
        return self.__judul
    
    def pinjam(self, nama):
        return f"{nama} berhasil meminjam buku fiksi berjudul {self.__judul}."
    
    def reservasi(self, nama):
        return f"{nama} telah berhasil reservasi buku fiksi {self.__judul}."
