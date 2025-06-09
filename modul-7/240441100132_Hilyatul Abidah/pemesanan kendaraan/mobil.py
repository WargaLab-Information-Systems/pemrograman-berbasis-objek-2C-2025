from kendaraan_interface import KendaraanInterface

class Mobil(KendaraanInterface):
    def __init__(self):
        self.biaya = 500_000
        self.usia_minimal = 22

    def validasi_usia(self, usia: int) -> bool:
        return usia >= self.usia_minimal

    def proses_booking(self):
        print("Mobil berhasil dibooking.")

    def hitung_biaya(self) -> int:
        return self.biaya

    def info_asuransi(self):
        print("Asuransi mobil termasuk kerusakan dan kecelakaan.")
