class Pengiriman:
    def __init__(self, asal, tujuan):
        self.asal = asal
        self.tujuan = tujuan

    def estimasi_waktu(self):
        return 5  


class PengirimanDarat(Pengiriman):
    def __init__(self, asal, tujuan, jenis_kendaraan):
        super().__init__(asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan

    def estimasi_waktu(self):
        jenis = self.jenis_kendaraan.lower()
        if jenis == "motor":
            return 6
        elif jenis == "mobil":
            return 4
        return 5 


class PengirimanUdara(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        super().__init__(asal, tujuan)
        self.maskapai = maskapai

    def estimasi_waktu(self):
        maskapai = self.maskapai.lower()
        if maskapai == "garuda":
            return 2
        elif maskapai == "lion":
            return 3
        return 4  


class PengirimanInternasional(Pengiriman):
    def __init__(self, asal, tujuan, jenis_kendaraan, maskapai):
        super().__init__(asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan
        self.maskapai = maskapai

    def estimasi_waktu(self):
        darat = PengirimanDarat(self.asal, self.tujuan, self.jenis_kendaraan)
        udara = PengirimanUdara(self.asal, self.tujuan, self.maskapai)

        waktu_darat = darat.estimasi_waktu()
        waktu_udara = udara.estimasi_waktu()
        estimasi_awal = min(waktu_darat, waktu_udara)

        if "luar" in self.tujuan.lower():
            return estimasi_awal + 3
        return estimasi_awal


def main():
    print("=== Sistem Estimasi Pengiriman ===")
    asal = input("\nMasukkan asal pengiriman: ")
    tujuan = input("Masukkan tujuan pengiriman: ")

    while True:
        print("\nJenis pengiriman:")
        print("1. Darat")
        print("2. Udara")
        print("3. Internasional")
        print("Ketik 'selesai' untuk keluar.")
        pilihan = input("Pilihan Anda: ").strip().lower()

        if pilihan == "selesai":
            print("Program selesai.")
            break

        if pilihan == "1" or pilihan == "darat":
            kendaraan = input("Jenis kendaraan (motor/mobil): ")
            pengiriman = PengirimanDarat(asal, tujuan, kendaraan)
        elif pilihan == "2" or pilihan == "udara":
            maskapai = input("Maskapai: ")
            pengiriman = PengirimanUdara(asal, tujuan, maskapai)
        elif pilihan == "3" or pilihan == "internasional":
            kendaraan = input("Jenis kendaraan (motor/mobil): ")
            maskapai = input("Maskapai (garuda/lion): ")
            pengiriman = PengirimanInternasional(asal, tujuan, kendaraan, maskapai)
        else:
            print("Pilihan tidak dikenali. Coba lagi.")
            continue

        print(f"\nEstimasi waktu pengiriman dari {asal} ke {tujuan}: {pengiriman.estimasi_waktu()} hari")

if __name__ == '__main__':
    main()
