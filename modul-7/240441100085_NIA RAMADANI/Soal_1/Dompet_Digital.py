from Metode_Pembayaran import MetodePembayaran

class DompetDigital(MetodePembayaran):
    def hitung_total(self):
        return self.jumlah

    def bayar(self):
        cashback = self.jumlah * 0.02
        total = self.hitung_total()
        sisa = self.saldo_awal - total + cashback
        print("\n=== RINCIAN PEMBAYARAN (Dompet Digital) ===")
        print(f"Total Belanja             : Rp{self.jumlah:,.0f}")
        print(f"Cashback 2%               : +Rp{cashback:,.0f}")
        print(f"Jumlah yang Dibayar       : Rp{total:,.0f}\n")
        print(f"Saldo Awal                : Rp{self.saldo_awal:,.0f}")
        print(f"Sisa Saldo                : Rp{sisa:,.0f}")
        print("============================================")
