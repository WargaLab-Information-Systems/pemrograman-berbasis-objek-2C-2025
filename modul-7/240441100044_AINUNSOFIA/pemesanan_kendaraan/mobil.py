from booking import Booking
from biaya import Biaya
from asuransi import Asuransi

class Mobil(Booking, Biaya, Asuransi):
    def proses_booking(self, nama: str, usia: int):
        if usia < 21:
            print(f"[Mobil] Maaf {nama}, usia minimal untuk menyewa mobil adalah 21 tahun.")
            return False
        print(f"[Mobil] Booking berhasil untuk {nama}.")
        return True

    def hitung_biaya(self, durasi: int) -> float:
        if durasi <= 0:
            raise ValueError("Durasi harus lebih dari 0")
        return 250000 * durasi

    def hitung_asuransi(self) -> float:
        return 50000
