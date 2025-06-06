class Buku:
    def __init__(self, judul, penulis, halaman):
        self.__judul = judul
        self.__penulis = penulis
        self.__halaman = halaman

    def get_judul(self):
        return self.__judul

    def get_penulis(self):
        return self.__penulis
    
    def get_halaman(self):
        return self.__halaman


class Perpustakaan:
    def __init__(self):
        self._daftar_buku = []

    def tambah_buku(self, buku):
        self._daftar_buku.append(buku)
        print(f"Buku '{buku.get_judul()}' berhasil ditambahkan.")

    def tampilkan_buku(self):
        if not self._daftar_buku:
            print("Belum ada buku dalam perpustakaan.")
            return

        print("\nDaftar Buku di Perpustakaan:")
        print("-" * 30)
        for idx, b in enumerate(self._daftar_buku, start=1):
            print(f"{idx}. Judul   : {b.get_judul()}")
            print(f"   Penulis : {b.get_penulis()}")
            print(f"   Halaman : {b.get_halaman()} halaman")
            print("-" * 30)

perpus = Perpustakaan()

perpus.tambah_buku(Buku("Laskar Pelangi", "Andrea Hirata", 534))
perpus.tambah_buku(Buku("Bumi Manusia", "Pramoedya Ananta Toer", 472))
perpus.tambah_buku(Buku("Atomic Habits", "James Clear", 320))

perpus.tampilkan_buku()