from vehicles.kendaraan import Kendaraan

class Sepeda(Kendaraan):
    def proses_booking(self, user):
        if user.usia < 10:
            raise ValueError("Usia minimal untuk menyewa sepeda adalah 10 tahun.")
        return f"{user.nama} berhasil memesan sepeda."

    def asuransi(self):
        return 0  