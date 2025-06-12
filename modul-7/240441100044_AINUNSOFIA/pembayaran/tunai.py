from payment import Payment

class Tunai(Payment):
    def proses_pembayaran(self, jumlah: float) -> float:
        diskon = 0.05  # 5% diskon
        total = jumlah * (1 - diskon)
        print(f"[Tunai] Diskon 5% diterapkan. Total bayar: Rp{total}")