from interface.booking import Booking
from interface.biaya import Biaya
from interface.asuransi import Asuransi

class Mobil(Booking, Biaya, Asuransi):
    def __init__(self):
        self.biaya_sewa = 300000
        self.asuransi = 50000

    def proses_booking(self, nama, usia):
        if usia >= 18:
            print("\n--- BOOKING MOOBIL ---")
            print("Booking mobil berhasil !!!!!")
            print(f"nama pembooking : Tn/Nn {nama}")
            print(f"usia pembooking : {usia} tahun")
            return True
        elif usia < 18:
            print("\n-- Usia minimal untuk menyewa mobil adalah 18 tahun --")
            return False
        else:
            print("\n-- Inputan anda tidak valid --")

    def hitung_biaya(self):
        return self.biaya_sewa

    def biaya_asuransi(self):
        return self.asuransi
