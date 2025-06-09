from interfacePembayaran import Pembayaran

class KartuKredit(Pembayaran):
    def prosesPembayaran(self, jumlah):
        biayaAdmin = 0.02 * jumlah
        return jumlah + biayaAdmin
    