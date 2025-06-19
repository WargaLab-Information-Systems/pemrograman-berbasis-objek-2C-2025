from books.buku import Buku
from interfaces.reservasi import Reservasi

class BukuReferensi(Buku, Reservasi):
    def __init__(self, judul, penulis):
        super().__init__(judul, penulis)
        self._status = "hanya bisa dibaca di tempat"

    def reservasi(self):
        if not self._dipesan:
            self._dipesan = True
            print(f"Buku referensi '{self._judul}' berhasil dipesan untuk dibaca di tempat.")
        else:
            print(f"Buku referensi '{self._judul}' sudah dipesan.")

    def batalkan_reservasi(self):
        if self._dipesan:
            self._dipesan = False
            print(f"Reservasi buku referensi '{self._judul}' dibatalkan.")
        else:
            print(f"Tidak ada reservasi untuk buku referensi '{self._judul}'.")