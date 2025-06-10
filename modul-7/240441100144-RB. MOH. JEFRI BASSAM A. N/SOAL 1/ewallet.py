from Interface import MetodePembayaran

class EWallet(MetodePembayaran):
    def proses_pembayaran(self, jumlah):
        cashback = 0.1 * jumlah
        total = jumlah - cashback
        print("\n-- E-WALLET --")
        print(f"Selamatt!!! Kamu dapat casback Rp{cashback} yuuhuuu, diberikan setelah pembayaran")
        print(f"Total bayar dari Rp{jumlah} menjadi Rp{total}")
        return total
