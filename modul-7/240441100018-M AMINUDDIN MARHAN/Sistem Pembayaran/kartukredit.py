from sistempembayaran import SistemPembayaran
class KartuKredit(SistemPembayaran):
    def __init__(self, jumlah):
        if not isinstance(jumlah, (float, int)) or jumlah <= 0:
            raise ValueError("Jumlah harus berupa angka positif")
        self.__jumlah = jumlah

    @property
    def jumlah(self):
        return self.__jumlah
    
    def bayar(self):
        print("=== Metode Kartu Kredit ===")
        print(f"Total belanja anda Rp.{self.jumlah}")
        biaya_admin = 0.02 * self.jumlah
        print(f"Tambahan biaya admin sebesar Rp.{biaya_admin}")
        return self.jumlah + biaya_admin