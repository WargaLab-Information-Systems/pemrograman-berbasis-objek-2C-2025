from kendaraan_interface import KendaraanInterface

class Sepeda(KendaraanInterface):
    def __init__(self):
        self.biaya = 50_000
        self.usia_minimal = 17

    def validasi_usia(self, usia: int) -> bool:
        return usia >= self.usia_minimal

    def proses_booking(self):
        print("Sepeda berhasil dibooking.")

    def hitung_biaya(self) -> int:
        return self.biaya

    def info_asuransi(self):
        print("Asuransi sepeda hanya untuk kerusakan.")
