from interface import BookingInterface

class Mobil(BookingInterface):
    def proses_booking(self, nama, usia) :
        if usia < 21:
            print(f"{nama}, usia minimal untuk booking mobil adalah 21 tahun.")
            return False
        print(f"{nama} berhasil booking mobil.")
        return True
    def hitung_biaya(self):
        return 500000

    def informasi_asuransi(self):
        return 200000
