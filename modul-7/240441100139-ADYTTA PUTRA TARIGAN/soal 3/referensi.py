from buku import Buku

class BukuReferensi(Buku):
    def __init__(self, judul, penulis):
        super().__init__(judul, penulis)

    def info(self):
        return f"[REFERENSI] {super().info()}"