from peminjaman import Peminjaman
from reservasi import Reservasi

class Bukufiksi(Peminjaman, Reservasi):
    def __init__(self):
        self.judul = ""
        self.status_pinjam = False

    def pinjaman(self):
        self.judul = input("masukkan judul buku yang ingin anda pinjam: ")
        if not self.status_pinjam:
            self.status_pinjam = True
            print(f"buku fiksi {self.judul} berhasil di pinjam")
        else:
            print(f"buku fiksi {self.judul} sedang dipinjam")
    def kembalikan(self):
        if self.status_pinjam:
            self.status_pinjam = False
            print(f"buku fiksi {self.judul} berhasil dikembalikan")
        else:
            print(f"buku fiksi {self.judul} belum dipinjam")

    def reservasi(self):
        print(f"buku fiksi {self.judul} berhasil di reservasi")
    
