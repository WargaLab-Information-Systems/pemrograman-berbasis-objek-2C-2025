from interfacePembayaran import Pembayaran

class DompetDigital(Pembayaran):
    def prosesPembayaran(self, jumlah):
        diskon = 0.02 * jumlah
        return jumlah - diskon