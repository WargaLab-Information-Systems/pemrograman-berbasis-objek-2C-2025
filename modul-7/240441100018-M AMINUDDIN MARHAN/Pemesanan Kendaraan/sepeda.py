from pemesanan import PemesananKendaraan
class Sepeda(PemesananKendaraan):
    def __init__(self):
        self.__usia = 0

    @property
    def usia(self):
        return self.__usia
    
    def input(self):
        while True:
            try:
                self.__usia = int(input("Masukkan usia untuk booking sepeda: "))
                if self.__usia <= 0:
                    print("Usia tidak boleh 0 atau kurang")
                break
            except ValueError:
                print("Input harus bertipe integer")
    
    def booking(self):
        if self.__usia >= 6:
            return "Sepeda berhasil dibooking"
        return "Usia anda belum mencukupi"
    
    def biaya(self):
        if self.__usia >= 6:
            print(f"Harga Rp. {2000000}")
    
    def asuransi(self):
        if self.__usia >= 6:
            print("Asuransi sepeda aktif selama 1 tahun")