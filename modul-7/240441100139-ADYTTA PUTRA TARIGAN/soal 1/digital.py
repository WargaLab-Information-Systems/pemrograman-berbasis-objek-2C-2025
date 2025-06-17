class PembayaranDompetDigital:
    def bayar(self, total, dibayar):
        cashback = 0.02
        cashback_amount = int(total * cashback)

        print("Metode pembayaran: Dompet Digital")
        print("Pembayaran melalui dompet digital mendapatkan cashback 2%.")
        print(f"Total belanja: Rp{total}")
        print(f"Cashback yang Anda dapatkan: Rp{cashback_amount}")

        if dibayar < total:
            print("Pembayaran gagal: jumlah yang dibayarkan kurang dari total belanja.")
            return

        kembalian = dibayar - total
        print(f"Pembayaran berhasil. Jumlah dibayarkan: Rp{dibayar}")
        print(f"Kembalian: Rp{kembalian}")
