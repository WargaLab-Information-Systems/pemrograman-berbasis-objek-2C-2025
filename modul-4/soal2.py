class Buku:
    def __init__(self, judul, penulis, halaman):
        self.__judul = judul
        self.__penulis = penulis
        self.__halaman = halaman

    def get_info(self):
        return f"Judul: {self.__judul}, Penulis: {self.__penulis}, Halaman: {self.__halaman}"


class Perpustakaan:
    def __init__(self):
        self.buku_list = []

    def tambah_buku(self, buku):
        self.buku_list.append(buku)

    def tampilkan_buku(self):
        print("=== DAFTAR BUKU ===")
        for b in self.buku_list:
            print(b.get_info())

perpus = Perpustakaan()

b1 = Buku("OLIVER ROBERT ELVANO", "sereneblues", 325)
b2 = Buku("ANTARA HARAPAN DAN KENYATAAN", "sereneblues", 237)

perpus.tambah_buku(b1)
perpus.tambah_buku(b2)

perpus.tampilkan_buku()
