from interfaces import Peminjaman

class BukuPelajaran(Peminjaman):
    def __init__(self):
        self.jenis = "Buku Pelajaran"
        self.maxPinjam = 7
        self.denda_per_hari = 2000

    def info_buku(self):
        print(f"\n--- {self.jenis} ----")
        print(f"Maksimal pinjam : {self.maxPinjam} hari")
        print(f"Denda/hari      : Rp{self.denda_per_hari}")

    def hitung_denda(self, lama_pinjam):
        if lama_pinjam > self.maxPinjam:
            return (lama_pinjam - self.maxPinjam) * self.denda_per_hari
        else:
            return 0
