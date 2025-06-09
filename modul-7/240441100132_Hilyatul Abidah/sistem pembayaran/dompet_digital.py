from metode import MetodePembayaran

class DompetDigital(MetodePembayaran):
    def proses_pembayaran(self, jumlah: int) -> int:
        potongan = int(0.10 * jumlah)
        print(f"Dompet Digital mendapatkan potongan 10%: {potongan}")
        return jumlah - potongan
