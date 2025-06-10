from interface.booking import Booking
from interface.biaya import Biaya
from interface.asuransi import Asuransi

class Motor(Booking, Biaya, Asuransi):
    def __init__(self):
        self.biaya_sewa = 150000
        self.asuransi = 25000

    def proses_booking(self, nama, usia):
        if usia >= 17:
            print("\n--- BOOKING MOTOR ---")
            print("Booking motor berhasil !!!!!")
            print(f"nama pembooking : Tn/Nn {nama}")
            print(f"usia pembooking : {usia} tahun")
            return True
        elif usia < 17:
            print("\n-- Usia minimal untuk menyewa motor adalah 17 tahun --")
            return False
        else:
            print("\n-- Inputan anda tidak valid --")

    def hitung_biaya(self) -> float:
        return self.biaya_sewa

    def biaya_asuransi(self) -> float:
        return self.asuransi
