class PembayaranTunai:
    def bayar(self, total, dibayar):
        diskon = 0.05
        total_setelah_diskon = int(total * (1 - diskon))
        
        print("Metode pembayaran: Tunai")
        print("Anda mendapatkan diskon 5% karena menggunakan tunai.")
        print(f"Total sebelum diskon: Rp{total}")
        print(f"Total setelah diskon: Rp{total_setelah_diskon}")

        if dibayar < total_setelah_diskon:
            print("Pembayaran gagal: jumlah yang dibayarkan kurang dari total setelah diskon.")
            return

        kembalian = dibayar - total_setelah_diskon
        print(f"Pembayaran berhasil. Jumlah dibayarkan: Rp{dibayar}")
        print(f"Kembalian: Rp{kembalian}")