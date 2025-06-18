from Metode_Pembayaran import MetodePembayaran

class KartuKredit(MetodePembayaran):
    def hitung_total(self):
        biaya = 0.03
        return self.jumlah * (1 + biaya)

    def bayar(self):
        total = self.hitung_total()
        sisa = self.saldo_awal - total
        print("\n=== RINCIAN PEMBAYARAN (Kartu Kredit) ===")
        print(f"Total Belanja             : Rp{self.jumlah:,.0f}")
        print(f"Biaya Tambahan 3%         : +Rp{self.jumlah * 0.03:,.0f}")
        print(f"Jumlah yang Harus Dibayar : Rp{total:,.0f}\n")
        print(f"Saldo Awal                : Rp{self.saldo_awal:,.0f}")
        print(f"Sisa Saldo                : Rp{sisa:,.0f}")
        print("==========================================")
