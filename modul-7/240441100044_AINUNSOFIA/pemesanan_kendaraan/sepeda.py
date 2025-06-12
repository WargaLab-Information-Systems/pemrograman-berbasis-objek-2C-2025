from booking import Booking
from biaya import Biaya
from asuransi import Asuransi

class Sepeda(Booking, Biaya, Asuransi):
    def proses_booking(self, nama: str, usia: int):
        if usia < 10:
            print(f"[Sepeda] Maaf {nama}, usia minimal untuk menyewa sepeda adalah 10 tahun.")
            return False
        print(f"[Sepeda] Booking berhasil untuk {nama}.")
        return True

    def hitung_biaya(self, durasi: int) -> float:
        return 50000 * durasi

    def hitung_asuransi(self) -> float:
        return 10000