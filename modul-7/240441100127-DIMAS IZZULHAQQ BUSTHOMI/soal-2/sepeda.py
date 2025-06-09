from interfacePemesanan import Booking

class Sepeda(Booking):
    def __init__(self):
        self.__harga = 100000
        self.__asuransi = 15000
    
    def proses_booking(self, nama, usia):
        if usia < 10:
            return f"{nama}, usia minimal untuk menyewa sepeda adalah 10 tahun."
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