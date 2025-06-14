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

    def tambah_buku(self, judul, penulis, jumlah_halaman):
        buku_baru = Buku(judul, penulis, jumlah_halaman)
        self.daftar_buku.append(buku_baru)
        print(f"Buku '{judul}' berhasil ditambahkan.")

    def tampilkan_buku(self):
        if not self.daftar_buku:
            print("Belum ada buku di perpustakaan.")
            return
        
        print("\nDaftar Buku di Perpustakaan:")
        for i, buku in enumerate(self.daftar_buku, 1):
            print(f"{i}. Judul: {buku.get_judul()}, Penulis: {buku.get_penulis()}, Halaman: {buku.get_jumlah_halaman()}")


def main():
    perpus = Perpustakaan()

    perpus.tambah_buku("Laskar Pelangi", "Andrea Hirata", 529)
    perpus.tambah_buku("Negeri 5 Menara", "Ahmad Fuadi", 430)
    perpus.tambah_buku("Atomic Habits", "James Clear", 320)

    perpus.tampilkan_buku()


if __name__ == "__main__":
    main()