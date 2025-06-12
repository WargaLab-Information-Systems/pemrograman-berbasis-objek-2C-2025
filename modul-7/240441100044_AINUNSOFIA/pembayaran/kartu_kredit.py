from payment import Payment

class KartuKredit(Payment):
    def proses_pembayaran(self, jumlah: float) -> float:
        biaya_admin = 2500  # Biaya tambahan tetap
        total = jumlah + biaya_admin
        print(f"[Kartu Kredit] Biaya admin Rp2500 ditambahkan. Total bayar: Rp{total}")
