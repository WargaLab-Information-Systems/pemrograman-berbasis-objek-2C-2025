from interfacePemesanan import Booking

class Motor(Booking):
    def __init__(self):
        self.__harga = 250000
        self.__asuransi = 50000

    def proses_booking(self, nama, usia):
        if usia < 18:
            return f"{nama}, usia minimal untuk menyewa motor adalah 18 tahun."
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