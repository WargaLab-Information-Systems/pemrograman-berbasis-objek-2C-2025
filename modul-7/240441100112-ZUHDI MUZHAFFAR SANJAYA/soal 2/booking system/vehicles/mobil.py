from vehicles.kendaraan import Kendaraan

class Mobil(Kendaraan):
    def proses_booking(self, user):
        if user.usia < 21:
            raise ValueError("Usia minimal untuk menyewa mobil adalah 21 tahun.")
        return f"{user.nama} berhasil memesan mobil."

    def asuransi(self):
        return 0.2 * self._harga_per_hari 