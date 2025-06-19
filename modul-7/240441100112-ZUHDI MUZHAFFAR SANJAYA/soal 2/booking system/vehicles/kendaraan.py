from interface.booking_interface import BookingInterface

class Kendaraan(BookingInterface):
    def __init__(self, nama, harga_per_hari):
        self._nama = nama
        self._harga_per_hari = harga_per_hari

    def hitung_biaya(self):
        return self._harga_per_hari

    def asuransi(self):
        return 0.1 * self._harga_per_hari  