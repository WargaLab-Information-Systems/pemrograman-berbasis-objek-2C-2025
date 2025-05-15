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
        buku = Buku(judul, penulis, jumlah_halaman)
        self.daftar_buku.append(buku)

    def tampilkan_buku(self):
        print("=== Daftar Buku ===")
        for b in self.daftar_buku:
            print(f"Judul: {b.judul}, Penulis: {b.penulis}, Jumlah Halaman: {b.jumlah_halaman}")


perpus = Perpustakaan()
perpus.tambah_buku("Ambalan 1969", "Ambatukam", 9696)
perpus.tambah_buku("Tung Tung Tung Sahur", "Anomali", 911)
perpus.tampilkan_buku()