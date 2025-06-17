class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        self.tersedia = True

    def info(self):
        return f"{self.judul} oleh {self.penulis} - {'Tersedia' if self.tersedia else 'Dipinjam'}"