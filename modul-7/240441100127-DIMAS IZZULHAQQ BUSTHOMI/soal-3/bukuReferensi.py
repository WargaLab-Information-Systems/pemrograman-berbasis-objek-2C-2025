from peminjamanInterface import Peminjaman
from reservasiInterface import Reservasi

class BukuReferensi(Peminjaman, Reservasi):
    def __init__(self, judul):
        self.__judul = judul

    @property
    def judul(self):
        return self.__judul
    
    def pinjam(self, nama):
        return f"Maaf {nama}, buku referensi {self.__judul} tidak dapat dipinjam. Hanya untuk dibaca di tempat."
    
    def reservasi(self, nama):
        return f"{nama} telah berhasil reservasi buku referensi {self.__judul}."
