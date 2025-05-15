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
        self.daftar_buku = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)
        print(f"Buku '{buku.get_judul()}' berhasil ditambahkan ke perpustakaan.")

    def tampilkan_semua_buku(self):
        print("\nDaftar Buku di Perpustakaan:")
        if not self.daftar_buku:
            print("Belum ada buku yang ditambahkan.")
        else:
            for i, buku in enumerate(self.daftar_buku, start=1):
                print(f"{i}. Judul: {buku.get_judul()}, Penulis: {buku.get_penulis()}, Jumlah Halaman: {buku.get_jumlah_halaman()}")


def main():
    perpustakaan = Perpustakaan()

    buku1 = Buku("Matematika", "Andrea Hirata", 529)
    buku2 = Buku("IPA", "Ahmad Fuadi", 424)
    buku3 = Buku("PPKN", "Tere Liye", 440)

    perpustakaan.tambah_buku(buku1)
    perpustakaan.tambah_buku(buku2)
    perpustakaan.tambah_buku(buku3)

    perpustakaan.tampilkan_semua_buku()

main()
