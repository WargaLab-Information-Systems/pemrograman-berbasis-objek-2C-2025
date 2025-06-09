from buku import Buku
from interface_peminjaman import PeminjamanInterface
from interface_reservasi import ReservasiInterface

class BukuReferensi(Buku, PeminjamanInterface, ReservasiInterface):
    def __init__(self, judul, pengarang):
        super().__init__(judul, pengarang)

    def pinjam(self):
        print(f"Buku referensi '{self.judul}' tidak bisa dipinjam.")

    def reservasi(self):
        print(f"Buku referensi '{self.judul}' berhasil direservasi.")
