from booking import Booking
from biaya import Biaya
from asuransi import Asuransi

class Motor(Booking, Biaya, Asuransi):
    def proses_booking(self, nama: str, usia: int):
        if usia < 17:
            print(f"[Motor] Maaf {nama}, usia minimal untuk menyewa motor adalah 17 tahun.")
            return False
        print(f"[Motor] Booking berhasil untuk {nama}.")
        return True

    def hitung_biaya(self, durasi: int) -> float:
        return 100000 * durasi

    def hitung_asuransi(self) -> float:
        return 20000