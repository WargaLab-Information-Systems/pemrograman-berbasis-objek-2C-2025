class PembayaranKartuKredit:
    def bayar(self, total, dibayar):
        bunga = 0.03
        total_setelah_bunga = int(total * (1 + bunga))

        print("Metode pembayaran: Kartu Kredit")
        print("Transaksi menggunakan kartu kredit dikenakan bunga 3%.")
        print(f"Total sebelum bunga: Rp{total}")
        print(f"Total setelah bunga: Rp{total_setelah_bunga}")

        if dibayar < total_setelah_bunga:
            print("Pembayaran gagal: jumlah yang dibayarkan kurang dari total setelah bunga.")
            return

        kembalian = dibayar - total_setelah_bunga
        print(f"Pembayaran berhasil. Jumlah dibayarkan: Rp{dibayar}")
        print(f"Kembalian: Rp{kembalian}")
