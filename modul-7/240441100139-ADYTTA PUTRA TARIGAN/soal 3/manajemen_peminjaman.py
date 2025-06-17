class ManajemenPeminjaman:
    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)

    def tampilkan_semua_buku(self):
        if not self.daftar_buku:
            print("Belum ada buku.")
        else:
            for i, buku in enumerate(self.daftar_buku, 1):
                print(f"{i}. {buku.info()}")

    def ambil_buku(self, indeks):
        if 0 <= indeks < len(self.daftar_buku):
            return self.daftar_buku[indeks]
        else:
            raise IndexError("Indeks di luar jangkauan.")
