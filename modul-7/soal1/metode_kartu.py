from interface import PaymentMethod

class KartuKredit(PaymentMethod):
    def proses_pembayaran(self, jumlah: float):
        biaya_admin = 3000  # Biaya tetap
        total = jumlah + biaya_admin
        print(f"Metode: Kartu Kredit | Biaya Admin Rp3.000 | Total dibayar: Rp{total:,.2f}")
        return total
