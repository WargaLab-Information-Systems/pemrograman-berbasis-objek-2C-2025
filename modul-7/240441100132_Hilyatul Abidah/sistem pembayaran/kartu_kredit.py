from metode import MetodePembayaran

class KartuKredit(MetodePembayaran):
    def proses_pembayaran(self, jumlah: int) -> int:
        potongan = int(0.05 * jumlah)
        print(f"Kartu Kredit mendapatkan potongan 5%: {potongan}")
        return jumlah - potongan
