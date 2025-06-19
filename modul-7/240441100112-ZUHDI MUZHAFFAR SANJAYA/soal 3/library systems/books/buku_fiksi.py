from books.buku import Buku
from interfaces.peminjaman import Peminjaman
from interfaces.reservasi import Reservasi

class BukuFiksi(Buku, Peminjaman, Reservasi):
    def pinjam(self):
        if self._status == "tersedia":
            self._status = "dipinjam"
            print(f"Buku '{self._judul}' berhasil dipinjam.")
        else:
            print(f"Buku '{self._judul}' tidak tersedia untuk dipinjam.")

    def kembalikan(self):
        if self._status == "dipinjam":
            self._status = "tersedia"
            print(f"Buku '{self._judul}' telah dikembalikan.")
        else:
            print(f"Buku '{self._judul}' tidak sedang dipinjam.")

    def reservasi(self):
        if not self._dipesan:
            self._dipesan = True
            print(f"Buku '{self._judul}' berhasil dipesan untuk dibaca di tempat.")
        else:
            print(f"Buku '{self._judul}' sudah dipesan.")

    def batalkan_reservasi(self):
        if self._dipesan:
            self._dipesan = False
            print(f"Reservasi buku '{self._judul}' dibatalkan.")
        else:
            print(f"Tidak ada reservasi untuk buku '{self._judul}'.")