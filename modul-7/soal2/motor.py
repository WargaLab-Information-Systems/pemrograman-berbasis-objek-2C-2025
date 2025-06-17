from interface import BookingInterface

class Motor(BookingInterface):
    def proses_booking(self, nama, usia):
        if usia < 17:
            print(f"{nama}, usia minimal untuk booking motor adalah 17 tahun.")
            return False
        print(f"{nama} berhasil booking motor.")
        return True

    def hitung_biaya(self) :
        return 150000

    def informasi_asuransi(self):
        return 20000
