from Interface import MetodePembayaran

class KartuKredit(MetodePembayaran):
    def proses_pembayaran(self, jumlah):
        biaya_admin = 5000
        total = jumlah + biaya_admin
        print("\n-- KARTU KREDIT --")
        print(f"Kamu dikenakan biaya admin Rp5000 ya")
        print(f"Total bayar dari Rp{jumlah} menjadi Rp{total}")
        return total
