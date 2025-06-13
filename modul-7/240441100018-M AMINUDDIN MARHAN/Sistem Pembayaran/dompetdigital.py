from sistempembayaran import SistemPembayaran
class DompetDigital(SistemPembayaran):
    def __init__(self, jumlah):
        if not isinstance(jumlah, (float, int)) or jumlah <= 0:
            raise ValueError("Jumlah harus berupa angka positif")
        self.__jumlah = jumlah

    @property
    def jumlah(self):
        return self.__jumlah
    
    def bayar(self):
        print("=== Metode Dompet Digital ===")
        print(f"Total belanja anda Rp.{self.jumlah}")
        if self.jumlah > 300000:
            potongan = 0.1 * self.jumlah
            print(f"Terdapat potongan sebesar Rp.{potongan}")
            return self.jumlah - potongan
        else:
            return self.jumlah