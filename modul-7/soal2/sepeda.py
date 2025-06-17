from interface import BookingInterface

class Sepeda(BookingInterface):
    def proses_booking(self, nama, usia) :
        if usia < 12:
            print(f"{nama}, usia minimal untuk booking sepeda adalah 12 tahun.")
            return False
        print(f"{nama} berhasil booking sepeda.")
        return True
    def hitung_biaya(self):
        return 50000

    def informasi_asuransi(self) :
        return 5000
