class Pengiriman:
    def __init__(self, asal, tujuan):
        self.asal = asal
        self.tujuan = tujuan

    def waktu_pengiriman(self):
        return 5

class PengirimanDarat(Pengiriman):
    def __init__(self, asal, tujuan, jenis_kendaraan):
        super().__init__(asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan

    def waktu_pengiriman(self):
        if self.jenis_kendaraan == 1:
            return 3
        elif self.jenis_kendaraan == 2:
            return 4
        elif self.jenis_kendaraan == 3:
            return 7
        else:
            print("Tidak ada pilihan kendaraan")
            return 0

class PengirimanUdara(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        super().__init__(asal, tujuan)
        self.maskapai = maskapai

    def waktu_pengiriman(self):
        if self.maskapai == 1:
            return 1  
        elif self.maskapai == 2:
            return 2  
        else:
            print("Tidak ada pilihan maskapai")
            return 0

class PengirimanInternasional(Pengiriman):
    def __init__(self, asal, tujuan, jenis_kendaraan=None, maskapai=None):
        super().__init__(asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan
        self.maskapai = maskapai

    def estimasi_waktu(self):
        estimasi = 0

        if self.jenis_kendaraan:
            if self.jenis_kendaraan == 1:
                estimasi = 3
            elif self.jenis_kendaraan == 2:
                estimasi = 4
            elif self.jenis_kendaraan == 3:
                estimasi = 7
            else:
                return "Jenis kendaraan tidak valid"
            metode = f"dengan kendaraan {self.jenis_kendaraan}"
        elif self.maskapai:
            if self.maskapai == 1:
                estimasi = 1
            elif self.maskapai == 2:
                estimasi = 2
            else:
                return "Jenis maskapai tidak valid"
            metode = f"dengan maskapai {self.maskapai}"
        else:
            return "Metode pengiriman tidak valid"

        estimasi += 3
        return f"Estimasi pengiriman {metode} dari {self.asal} ke {self.tujuan} adalah {estimasi} hari."


while True:
    asal = input("Masukkan asal pengiriman: ")
    tujuan = input("Masukkan tujuan pengiriman: ")
    internasional = input("Apakah pengiriman internasional (y/n): ")

    kendaraan = None
    maskapai = None

    if internasional == "y":
        while True:
            print("\nPilih maskapai:")
            print("1. Garuda")
            print("2. Lion Air")
            maskapai_input = input("Masukkan pilihan maskapai (1/2): ")
            if maskapai_input in ["1", "2"]:
                maskapai = int(maskapai_input)
                break
            else:
                print("Tidak ada pilihan.")

        pengiriman = PengirimanInternasional(asal, tujuan, maskapai=maskapai)
        print("\n" + pengiriman.estimasi_waktu())
        break
    elif internasional == "n":
        while True:
            print("\nPilih jenis kendaraan:")
            print("1. Motor")
            print("2. Mobil")
            print("3. Truk")
            kendaraan_input = input("Masukkan pilihan kendaraan (1/2/3): ")
            if kendaraan_input in ["1", "2", "3"]:
                kendaraan = int(kendaraan_input)
                break
            else:
                print("Tidak ada dalam pilihan.")

        pengiriman = PengirimanDarat(asal, tujuan, kendaraan)
        print(f"\nEstimasi waktu pengiriman: {pengiriman.waktu_pengiriman()} hari")

    else:
        print("Pilihan internasional tidak valid.")