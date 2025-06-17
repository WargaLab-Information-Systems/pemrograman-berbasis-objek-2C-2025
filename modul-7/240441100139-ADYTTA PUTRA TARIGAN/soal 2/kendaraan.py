from booking import Booking

class Kendaraan(Booking):
    def __init__(self, nama_kendaraan, harga):
        self._nama_kendaraan = nama_kendaraan
        self._harga = harga

    def hitung_biaya(self):
        return self._harga

    def info_asuransi(self):
        return f"Asuransi untuk {self._nama_kendaraan} berlaku 1 tahun"

    def proses_booking(self, nama, usia):
        return f"Booking kendaraan {self._nama_kendaraan} berhasil untuk {nama} (usia {usia})"
