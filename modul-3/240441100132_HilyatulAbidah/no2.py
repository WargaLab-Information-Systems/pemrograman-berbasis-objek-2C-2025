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
        if self.jenis_kendaraan == "mobil":
            return 7
        elif self.jenis_kendaraan == "truk":
            return 10
        return 5

class PengirimanUdara(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        super().__init__(asal, tujuan)
        self.maskapai = maskapai

    def estimasi_waktu(self):
        if self.maskapai == "garuda":
            return 3
        elif self.maskapai == "air asia":
            return 4
        return 5

class PengirimanInternasional(PengirimanUdara):
    def estimasi_waktu(self):
        return super().estimasi_waktu() + 3  

pengiriman_list = []

while True:
    asal = input("Asal: ")
    tujuan = input("Tujuan: ")
    jenis_pengiriman = input("Apakah pengiriman internasional atau nasional? ").lower()

    if jenis_pengiriman == "internasional":
        maskapai = input("Maskapai (garuda/air asia): ").lower()
        pengiriman = PengirimanInternasional(asal, tujuan, maskapai)

    elif jenis_pengiriman == "nasional":
        tipe = input("Tipe pengiriman (darat/udara): ").lower()
        if tipe == "darat":
            kendaraan = input("Jenis kendaraan (mobil/truk): ").lower()
            pengiriman = PengirimanDarat(asal, tujuan, kendaraan)
        elif tipe == "udara":
            maskapai = input("Maskapai (garuda/air asia): ").lower()
            pengiriman = PengirimanUdara(asal, tujuan, maskapai)
        else:
            print("Tipe pengiriman tidak valid.")
            continue

    else:
        print("Jenis pengiriman tidak valid.")
        continue

    pengiriman_list.append(pengiriman)
    print(f"Estimasi waktu pengiriman: {pengiriman.estimasi_waktu()} hari")

    if input("Tambah pengiriman lagi? (y/n): ").lower() != "y":
        break

print("\nDaftar Semua Pengiriman:")
for i, pengiriman in enumerate(pengiriman_list, 1):
    print(f"Pengiriman {i}: {pengiriman.estimasi_waktu()} hari")