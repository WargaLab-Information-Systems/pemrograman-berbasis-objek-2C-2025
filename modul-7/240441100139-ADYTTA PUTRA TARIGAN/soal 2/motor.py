from kendaraan import Kendaraan

class Motor(Kendaraan):
    def __init__(self):
        super().__init__("Motor", 150000)

    def proses_booking(self, nama, usia):
        if usia < 17:
            return f"Gagal booking: usia {usia} terlalu muda untuk Motor (minimal 17)"
        return super().proses_booking(nama, usia)
