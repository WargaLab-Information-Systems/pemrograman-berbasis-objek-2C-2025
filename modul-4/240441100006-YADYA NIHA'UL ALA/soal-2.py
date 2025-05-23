class Buku:
    def __init__(self, judul, penulis, jumlah_halaman):
        self.__judul = judul
        self.__penulis = penulis
        self.__jumlah_halaman = jumlah_halaman

    def get_judul(self):
        return self.__judul

    def get_penulis(self):
        return self.__penulis

    def get_jumlah_halaman(self):
        return self.__jumlah_halaman


class Perpustakaan:
    def __init__(self):
        self.__daftar_buku = []

    def tambah_buku(self, buku):
        self.__daftar_buku.append(buku)
        print(f"{buku.get_judul()}, telah ditambahkan ke perpustakaan.")

    def tampilkan_buku(self):
        if not self.__daftar_buku:
            print("Belum ada buku di perpustakaan.")
            return
        print("Daftar Buku Perpustakaan:")
        print("⋆" * 35)
        for buku in self.__daftar_buku:
            print(f"Judul         : {buku.get_judul()}")
            print(f"Penulis       : {buku.get_penulis()}")
            print(f"Jumlah Halaman: {buku.get_jumlah_halaman()}")
            print("⋆" * 35)


def main():
    perpustakaan = Perpustakaan()

    perpustakaan.tambah_buku(Buku("Caraval", "Stephanie Garber", 407))
    perpustakaan.tambah_buku(Buku("Hujan", "Tere Liye", 320))
    perpustakaan.tambah_buku(Buku("Laut Bercerita", "Leila S. Chudori", 380))

    print("‣" * 35)
    perpustakaan.tampilkan_buku()


if __name__ == "__main__":
    main()