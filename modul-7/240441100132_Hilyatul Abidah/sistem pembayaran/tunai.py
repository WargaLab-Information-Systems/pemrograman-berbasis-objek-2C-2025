from metode import MetodePembayaran

class Tunai(MetodePembayaran):
    def proses_pembayaran(self, jumlah: int) -> int:
        potongan = int(0.07 * jumlah)
        print(f"Tunai mendapatkan potongan 7%: {potongan}")
        return jumlah - potongan
