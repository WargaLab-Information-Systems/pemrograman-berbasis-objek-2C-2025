from kendaraan import Kendaraan

class Mobil(Kendaraan):
    def __init__(self):
        super().__init__("Mobil", 500000)

    def proses_booking(self, nama, usia):
        if usia < 21:
            return f"Gagal booking: usia {usia} terlalu muda untuk Mobil (minimal 21)"
        return super().proses_booking(nama, usia)