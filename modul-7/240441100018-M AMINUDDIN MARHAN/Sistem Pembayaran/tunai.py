from sistempembayaran import SistemPembayaran
class Tunai(SistemPembayaran):
    def __init__(self, jumlah):
        if not isinstance(jumlah, (float, int)) or jumlah <= 0:
            raise ValueError("Jumlah harus berupa angka positif")
        self.__jumlah = jumlah

    @property
    def jumlah(self):
        return self.__jumlah

    def bayar(self):
        print("=== Metode Tunai ===")
        print(f"Total belanja anda Rp.{self.jumlah}")
        if self.jumlah >= 250000:
            diskon = 0.05 * self.jumlah
            print(f"Anda mendapatkan diskon sebesar Rp.{diskon}")
            return self.jumlah - diskon
        else:
            return self.jumlah