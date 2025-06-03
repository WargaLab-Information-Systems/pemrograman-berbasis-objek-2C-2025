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
        if self.jenis_kendaraan == 1:
            return 3
        elif self.jenis_kendaraan == 2:
            return 4
        elif self.jenis_kendaraan == 3:
            return 5
        elif self.jenis_kendaraan == 4:
            return 7
        else:
            return super().estimasi_waktu()

class PengirimanUdara(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        super().__init__(asal, tujuan)
        self.maskapai = maskapai

    def estimasi_waktu(self):
        if self.maskapai == 1:
            return 3
        elif self.maskapai == 2:
            return 4
        elif self.maskapai == 3:
            return 5
        else:
            return super().estimasi_waktu()

class PengirimanInternasional(PengirimanDarat, PengirimanUdara):
    def __init__(self, asal, tujuan, jenis_kendaraan, maskapai):
        Pengiriman.__init__(self, asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan
        self.maskapai = maskapai

    def estimasi_waktu(self):
        waktu_darat = PengirimanDarat(self.asal, self.tujuan, self.jenis_kendaraan).estimasi_waktu()
        waktu_udara = PengirimanUdara(self.asal, self.tujuan, self.maskapai).estimasi_waktu()
        waktu_tercepat = min(waktu_darat, waktu_udara)

        if self.tujuan.lower() != "dalam negeri":
            waktu_tercepat += 3
        elif self.tujuan.lower() != "luar negeri":
            return waktu_tercepat
        else:
            return waktu_tercepat

daftar_pengiriman = []
ke = 1

while True:
    print(f"\n--- Pengiriman ke-{ke} ---")
    asal = input("Masukkan asal pengiriman : ")

    print("\npilih tujuan pengirim:")
    print("1. Dalam Negeri")
    print("2. Luar Negeri")

    while True:
        tujuan = input("Masukkan tujuan pengiriman : ")
        if tujuan != 1 or tujuan != 2:
            break

    print("\npilih jenis kendaraan:")
    print("1. Mobil")
    print("2. motor")
    print("3. truck")
    print("4. sepeda")
    jenis_kendaraan = int(input("Masukkan jenis kendaraan (1/2/3/4): "))

    print("\npilih Maskapai:")
    print("1. Garuda Indonesia")
    print("2. Lion Air")
    print("3. Batik Air")
    maskapai = int(input("Masukkan maskapai (1/2/3): "))

    pngrm = PengirimanInternasional(asal, tujuan, jenis_kendaraan, maskapai)
    daftar_pengiriman.append(pngrm)

    lanjut = input("\nApakah Anda ingin menambahkan pengiriman lagi? (y/n): ")
    if lanjut != "y":
        break

    ke += 1

print("\n----- Estimasi waktu pengiriman -----")
for pengiriman in daftar_pengiriman:
    print(f"- {pengiriman.asal} to {pengiriman.tujuan} : selama {pengiriman.estimasi_waktu()} hari")