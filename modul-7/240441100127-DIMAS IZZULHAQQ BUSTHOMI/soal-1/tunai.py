from interfacePembayaran import Pembayaran

class Tunai(Pembayaran):
    def prosesPembayaran(self, jumlah):
        potongan = 0.05 * jumlah
        return jumlah - potongan
    