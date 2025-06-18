from Booking import Booking

class Mobil(Booking):
    def __init__(self, nama, usia):
        super().__init__(nama, usia)
        self.biaya = 500_000
        self.usia_min = 21

    def proses_pemesanan(self):
        self.cek_usia(self.usia_min)
        print(f"{self._nama} berhasil memesan Mobil.")

    def hitung_biaya(self):
        print(f"Biaya sewa Mobil: Rp{self.biaya:,}")
        return self.biaya

    def hitung_asuransi(self):
        asuransi = 50_000
        print(f"Asuransi Mobil: Rp{asuransi:,}")
        return asuransi
