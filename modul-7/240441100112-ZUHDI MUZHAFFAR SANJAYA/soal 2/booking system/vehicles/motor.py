from vehicles.kendaraan import Kendaraan

class Motor(Kendaraan):
    def proses_booking(self, user):
        if user.usia < 17:
            raise ValueError("Usia minimal untuk menyewa motor adalah 17 tahun.")
        return f"{user.nama} berhasil memesan motor."

    def asuransi(self):
        return 0.15 * self._harga_per_hari