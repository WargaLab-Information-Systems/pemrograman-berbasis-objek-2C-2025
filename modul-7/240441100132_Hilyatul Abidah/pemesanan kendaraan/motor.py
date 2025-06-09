from kendaraan_interface import KendaraanInterface

class Motor(KendaraanInterface):
    def __init__(self):
        self.biaya = 150_000
        self.usia_minimal = 19

    def validasi_usia(self, usia: int) -> bool:
        return usia >= self.usia_minimal

    def proses_booking(self):
        print("Motor berhasil dibooking.")

    def hitung_biaya(self) -> int:
        return self.biaya

    def info_asuransi(self):
        print("Asuransi motor meliputi kehilangan dan tabrakan.")
