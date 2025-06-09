from buku import Buku
from interface_peminjaman import PeminjamanInterface
from interface_reservasi import ReservasiInterface

class BukuFiksi(Buku, PeminjamanInterface, ReservasiInterface):
    def __init__(self, judul, pengarang):
        super().__init__(judul, pengarang)

    def pinjam(self):
        print(f"Buku fiksi '{self.judul}' berhasil dipinjam.")

    def reservasi(self):
        print(f"Buku fiksi '{self.judul}' berhasil direservasi.")
