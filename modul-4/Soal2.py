class Buku:
    def __init__(self, judul, penulis, halaman):
        self.__judul = judul
        self.__penulis = penulis
        self.__halaman = halaman

    @property
    def judul(self):
        return self.__judul

    @judul.setter
    def judul(self, value):
        self.__judul = value

    @property
    def penulis(self):
        return self.__penulis

    @penulis.setter
    def penulis(self, value):
        self.__penulis = value

    @property
    def halaman(self):
        return self.__halaman

    @halaman.setter
    def halaman(self, value):
        if isinstance(value, int) and value > 0:
            self.__halaman = value
        else:
            print("Jumlah halaman tidak valid")

    def info(self):
        print(f"Judul  : {self.__judul}")
        print(f"Penulis: {self.__penulis}")
        print(f"Halaman: {self.__halaman}")
        print("-" * 30)


class Perpustakaan:
    def __init__(self):
        self.__daftar_buku = []

    def tambah_buku(self, judul, penulis, halaman):
        buku = Buku(judul, penulis, halaman)
        self.__daftar_buku.append(buku)
        print(f"Buku {judul} berhasil ditambahkan")

    def tampilkan_buku(self):
        if not self.__daftar_buku:
            print("Tidak ada buku di perpustakaan")
        for buku in self.__daftar_buku:
            buku.info()


class Main:
    @staticmethod
    def run():
        perpustakaan = Perpustakaan()
        perpustakaan.tambah_buku("Bernadit sang sad boy", "Udin", 529)
        perpustakaan.tambah_buku("Wi wok detok", "Owi", 535)
        print("\nDaftar Buku:")
        perpustakaan.tampilkan_buku()


if __name__ == "__main__":
    Main.run()
