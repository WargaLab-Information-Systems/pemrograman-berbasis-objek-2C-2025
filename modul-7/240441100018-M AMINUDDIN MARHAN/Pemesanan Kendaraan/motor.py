from pemesanan import PemesananKendaraan
class Motor(PemesananKendaraan):
    def __init__(self):
        self.__usia = 0

    @property
    def usia(self):
        return self.__usia
    
    def input(self):
        while True:
            try:
                self.__usia = int(input("Masukkan usia untuk booking motor: "))
                if self.__usia <= 0:
                    print("Usia tidak boleh 0 atau kurang")
                break
            except ValueError:
                print("Input harus bertipe integer")
    
    def booking(self):
        if self.__usia >= 17:
            return "Sepeda motor berhasil dibooking"
        return "Usia anda belum mencukupi"
    
    def biaya(self):
        if self.__usia >= 17:
            print(f"Harga Rp. {24000000}")
    
    def asuransi(self):
        if self.__usia >= 17:
            print("Asuransi sepeda motor aktif selama 2 tahun")