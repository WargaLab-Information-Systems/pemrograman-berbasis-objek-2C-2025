from interface import PaymentMethod

class DompetDigital(PaymentMethod):
    def proses_pembayaran(self, jumlah: float):
        potongan = 10000 if jumlah >= 100000 else 0
        total = jumlah - potongan
        print(f"Metode: Dompet Digital | Potongan Rp{potongan:,.0f} | Total dibayar: Rp{total:,.2f}")
        return total
