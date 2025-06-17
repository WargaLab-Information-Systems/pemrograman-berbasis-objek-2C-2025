from kendaraan import Kendaraan

class Sepeda(Kendaraan):
    def __init__(self):
        super().__init__("Sepeda", 50000)

    def proses_booking(self, nama, usia):
        if usia < 10:
            return f"Gagal booking: usia {usia} terlalu muda untuk Sepeda (minimal 10)"
        return super().proses_booking(nama, usia)
