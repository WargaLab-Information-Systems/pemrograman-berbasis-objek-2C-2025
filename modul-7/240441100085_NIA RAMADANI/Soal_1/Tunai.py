from Metode_Pembayaran import MetodePembayaran

class Tunai(MetodePembayaran):
    def hitung_total(self):
        diskon = 0.05
        return self.jumlah * (1 - diskon)

    def bayar(self):
        total = self.hitung_total()
        sisa = self.saldo_awal - total
        print("\n=== RINCIAN PEMBAYARAN (Tunai) ===")
        print(f"Total Belanja             : Rp{self.jumlah:,.0f}")
        print(f"Diskon 5%                 : -Rp{self.jumlah * 0.05:,.0f}")
        print(f"Jumlah yang Harus Dibayar : Rp{total:,.0f}\n")
        print(f"Saldo Awal                : Rp{self.saldo_awal:,.0f}")
        print(f"Sisa Saldo                : Rp{sisa:,.0f}")
        print("===================================")
