class Buku:
    def __init__(self, judul, penulis, jumlah_halaman):
        self.__judul = judul
        self.__penulis = penulis
        self.__jumlah_halaman = jumlah_halaman

    @property
    def judul(self):
        return self.__judul

    @property
    def penulis(self):
        return self.__penulis
    
    @property
    def jumlah_halaman(self):
        return self.__jumlah_halaman


class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self, judul, penulis, jumlah_halaman):
        buku_baru = Buku(judul, penulis, jumlah_halaman)
        self.daftar_buku.append(buku_baru)
        print(f"Buku '{judul}' berhasil ditambahkan.")

    def tampilkan_semua_buku(self):
        if not self.daftar_buku:
            print("Tidak ada buku di perpustakaan.")
        else:
            print("\n=== Daftar Buku di Perpustakaan ===")
            for buku in self.daftar_buku:
                print(f"Judul: {buku.judul} | Penulis: {buku.penulis} | Jumlah Halaman: {buku.jumlah_halaman}")


def main():
    perpustakaan = Perpustakaan()

    perpustakaan.tambah_buku("dongeng si kancil", "dian wildan", 529)
    perpustakaan.tambah_buku("Harry Potter", "J.K. Rowling", 350)
    perpustakaan.tambah_buku("Bumi Manusia", "Pramoedya Ananta Toer", 480)

    perpustakaan.tampilkan_semua_buku()


if __name__ == "__main__":
    main()
