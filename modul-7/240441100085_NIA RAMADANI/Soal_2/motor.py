from Booking import Booking

class Motor(Booking):
    def __init__(self, nama, usia):
        super().__init__(nama, usia)
        self.biaya = 200_000
        self.usia_min = 18

    def proses_pemesanan(self):
        self.cek_usia(self.usia_min)
        print(f"{self._nama} berhasil memesan Motor.")

    def hitung_biaya(self):
        print(f"Biaya sewa Motor: Rp{self.biaya:,}")
        return self.biaya

    def hitung_asuransi(self):
        asuransi = 25_000
        print(f"Asuransi Motor: Rp{asuransi:,}")
        return asuransi
