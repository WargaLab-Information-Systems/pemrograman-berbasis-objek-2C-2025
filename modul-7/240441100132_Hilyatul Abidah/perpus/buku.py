class Buku:
    def __init__(self, judul: str, pengarang: str):
        self.judul = judul
        self.pengarang = pengarang

    def info(self):
        print(f"Buku: {self.judul} dikarang oleh {self.pengarang}")
