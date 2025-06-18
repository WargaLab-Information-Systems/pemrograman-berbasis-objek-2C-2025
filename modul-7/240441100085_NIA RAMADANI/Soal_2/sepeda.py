from Booking import Booking

class Sepeda(Booking):
    def __init__(self, nama, usia):
        super().__init__(nama, usia)
        self.biaya = 50_000
        self.usia_min = 12

    def proses_pemesanan(self):
        self.cek_usia(self.usia_min)
        print(f"{self._nama} berhasil memesan Sepeda.")

    def hitung_biaya(self):
        print(f"Biaya sewa Sepeda: Rp{self.biaya:,}")
        return self.biaya

    def hitung_asuransi(self):
        asuransi = 10_000
        print(f"Asuransi Sepeda: Rp{asuransi:,}")
        return asuransi
