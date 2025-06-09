from interfacePemesanan import Booking

class Mobil(Booking):
    def __init__(self):
        self.__harga = 1000000
        self.__asuransi = 150000
    
    def proses_booking(self, nama, usia):
        if usia < 21:
            return f"{nama}, usia minimal untuk menyewa mobil adalah 21 tahun."
        else:
            return (
            f"Booking mobil berhasil untuk {nama}.\n"
            f"Biaya sewa: Rp {self.biaya}\n"
            f"Asuransi: Rp {self.asuransi}"
        )

    @property
    def biaya(self):
        return self.__harga
    
    @property
    def asuransi(self):
        return self.__asuransi