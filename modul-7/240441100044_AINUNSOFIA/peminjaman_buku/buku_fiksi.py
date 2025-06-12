from buku import Buku
from peminjaman import Peminjaman
from reservasi import Reservasi

class BukuFiksi(Buku, Peminjaman, Reservasi):
    def pinjam(self, nama: str):
        print(f"{nama} berhasil meminjam buku fiksi '{self.judul}'.")

    def reservasi(self, nama: str):
        print(f"{nama} berhasil melakukan reservasi buku fiksi '{self.judul}'.")
