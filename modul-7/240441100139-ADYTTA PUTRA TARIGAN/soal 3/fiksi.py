from buku import Buku

class BukuFiksi(Buku):
    def __init__(self, judul, penulis):
        super().__init__(judul, penulis)

    def pinjam(self):
        if self.tersedia:
            self.tersedia = False
            print("Buku berhasil dipinjam.")
        else:
            print("Buku sedang tidak tersedia.")

    def kembalikan(self):
        self.tersedia = True
        print("Buku berhasil dikembalikan.")

    def info(self):
        return f"[FIKSI] {super().info()}"
