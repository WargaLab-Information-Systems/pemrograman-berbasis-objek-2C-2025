from interface.booking import Booking
from interface.biaya import Biaya
from interface.asuransi import Asuransi

class Sepeda(Booking, Biaya, Asuransi):
    def __init__(self):
        self.biaya_sewa = 50000
        self.asuransi = 0  # tidak perlu asuransi

    def proses_booking(self, nama, usia):
        if usia >= 10:
            print("\n--- BOOKING SEPEDA ---")
            print("Booking sepeda berhasil !!!!!")
            print(f"nama pembooking : Tn/Nn {nama}")
            print(f"usia pembooking : {usia} tahun")
            return True
        elif usia < 10:
            print("\n-- Usia minimal untuk menyewa motor adalah 10 tahun --")
            return False
        else:
            print("\n-- Inputan anda tidak valid --")

    def hitung_biaya(self):
        return self.biaya_sewa

    def biaya_asuransi(self):
        return self.asuransi
