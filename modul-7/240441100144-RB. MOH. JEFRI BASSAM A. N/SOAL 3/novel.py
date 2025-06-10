from interfaces import Peminjaman

class Novel(Peminjaman):
    def __init__(self):
        self.jenis = "Novel"
        self.maxPinjam = 5
        self.denda_per_hari = 3000

    def info_buku(self):
        print(f"\n--- {self.jenis} ----")
        print(f"Maksimal pinjam : {self.maxPinjam} hari")
        print(f"Denda/hari      : Rp{self.denda_per_hari}")

    def hitung_denda(self, lama_pinjam):
        if lama_pinjam > self.maxPinjam:
            return (lama_pinjam - self.maxPinjam) * self.denda_per_hari
        else:
            return 0
