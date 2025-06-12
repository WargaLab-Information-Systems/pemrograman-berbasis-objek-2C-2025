from buku import Buku
from reservasi import Reservasi

class BukuReferensi(Buku, Reservasi):
    def reservasi(self, nama: str):
        print(f"{nama} berhasil melakukan reservasi buku referensi '{self.judul}'.")

    # Tidak bisa dipinjam
    def pinjam(self, nama: str):
        print(f"Buku referensi '{self.judul}' tidak boleh dipinjam.")
