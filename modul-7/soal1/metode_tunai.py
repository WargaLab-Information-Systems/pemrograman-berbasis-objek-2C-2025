from interface import PaymentMethod

class Tunai(PaymentMethod):
    def proses_pembayaran(self, jumlah: float):
        diskon = 0.05  # 5% 
        total = jumlah * (1 - diskon)
        print(f"Metode: Tunai | Diskon 5% | Total dibayar: Rp{total:,.2f}")
        return total
