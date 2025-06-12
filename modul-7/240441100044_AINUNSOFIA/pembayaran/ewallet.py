from payment import Payment

class DompetDigital(Payment):
    def proses_pembayaran(self, jumlah: float) -> float:
        cashback = 0.03  # 3% cashback (langsung dikurangi)
        total = jumlah * (1 - cashback)
        print(f"[Dompet Digital] Cashback 3% diterapkan. Total bayar: Rp{total}")
