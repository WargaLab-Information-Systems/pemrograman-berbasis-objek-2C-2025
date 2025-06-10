from Interface import MetodePembayaran

class Tunai(MetodePembayaran):
    def proses_pembayaran(self, jumlah):
        potongan = 0.05 * jumlah
        total = jumlah - potongan
        print("\n-- TUNAI --")
        print(f"Selamatt!!! Kamu dapat diskon 5% yuuhuu")
        print(f"Total bayar dari Rp{jumlah} menjadi Rp{total}")
        return total
