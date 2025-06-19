class ManajemenBuku:
    def __init__(self):
        self.buku = []  

    def tambah_buku(self, buku):
        self.buku.append(buku)

    def tampilkan_semua(self):
        for buku in self.buku:
            print(f"{buku.judul} oleh {buku.penulis}")