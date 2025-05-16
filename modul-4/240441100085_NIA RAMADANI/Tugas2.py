class Buku:
    def __init__(self, judul, penulis, jumlah_halaman):
        self.__judul = judul
        self.__penulis = penulis
        self.__jumlah_halaman = jumlah_halaman

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
    def jumlah_halaman(self):
        return self.__jumlah_halaman

    @jumlah_halaman.setter
    def jumlah_halaman(self, value):
        self.__jumlah_halaman = value

class Perpustakaan:
    def __init__(self):
        self.__daftar_buku = []

    def tambah_buku(self, buku):
        self.__daftar_buku.append(buku)

    def tampilkan_buku(self):
        if not self.__daftar_buku:
            print("Belum ada buku yang terdaftar di perpustakaan.")
        else:
            print("Daftar Buku di Perpustakaan:\n")
            for i, buku in enumerate(self.__daftar_buku, start=1):
                print(f"Buku {i}:")
                print(f"  Judul          : {buku.judul}")
                print(f"  Penulis        : {buku.penulis}")
                print(f"  Jumlah Halaman : {buku.jumlah_halaman}")
                print()

class main():
    perpus = Perpustakaan()

    buku1 = Buku("Laskar Pelangi", "Andrea Hirata", 529)
    buku2 = Buku("Bumi", "Tere Liye", 440)

    buku2.judul = "Bumi (Edisi Revisi)"
    buku2.jumlah_halaman = 450

    perpus.tambah_buku(buku1)
    perpus.tambah_buku(buku2)

    perpus.tampilkan_buku()
