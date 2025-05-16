class Pengiriman:
    def __init__(self, asal, tujuan):
        self.asal = asal
        self.tujuan = tujuan
    def estimasi_waktu(self):
        return "Estimasi waktu pengiriman belum ditentukan."

class PengirimanDarat(Pengiriman):
    def __init__(self, asal, tujuan, jenis_kendaraan):
        super().__init__(asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan
    def estimasi_waktu(self):
        if self.jenis_kendaraan == 1:
            estimasi = 3
        elif self.jenis_kendaraan == 2:
            estimasi = 5
        elif self.jenis_kendaraan == 3:
            estimasi = 7
        else:
            return "Jenis kendaraan tidak valid."
        return f"Estimasi pengiriman dengan {self.jenis_kendaraan} dari {self.asal} ke {self.tujuan} adalah {estimasi} hari."

class PengirimanUdara(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        super().__init__(asal, tujuan)
        self.maskapai = maskapai
    def estimasi_waktu(self):
        if self.maskapai == 1:
            estimasi = 3
        elif self.maskapai == 2:
            estimasi = 5
        else:
            return "Maskapai tidak valid."
        return f"Estimasi pengiriman dengan maskapai {self.maskapai} dari {self.asal} ke {self.tujuan} adalah {estimasi} hari."

class PengirimanInternasional(PengirimanDarat, PengirimanUdara):
    def __init__(self, asal, tujuan, jenis_kendaraan=None, maskapai=None):
        Pengiriman.__init__(self, asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan
        self.maskapai = maskapai

    def estimasi_waktu(self):
        if self.jenis_kendaraan is not None:
            if self.jenis_kendaraan == 1:
                estimasi = 3
            elif self.jenis_kendaraan == 2:
                estimasi = 5
            elif self.jenis_kendaraan == 3:
                estimasi = 7
            else:
                return "Jenis kendaraan tidak valid."
            metode = f"dengan kendaraan {self.jenis_kendaraan}"
        elif self.maskapai is not None:
            if self.maskapai == 1:
                estimasi = 3
            elif self.maskapai == 2:
                estimasi = 5
            else:
                return "Maskapai tidak valid."
            metode = f"dengan maskapai {self.maskapai}"
        else:
            return "Metode pengiriman tidak lengkap."
        estimasi += 3
        return f"Estimasi pengiriman {metode} dari {self.asal} ke {self.tujuan} (Internasional) adalah {estimasi} hari."

daftar_pengiriman = []
while True:
    print()
    asal = input("Masukkan asal pengiriman: ")
    tujuan = input("Masukkan tujuan pengiriman: ")
    internasional = input("Apakah pengiriman internasional? (y/n): ").lower()
    if internasional == "y":
        if internasional == "y":
            print("1. Air Asia")
            print("2. Sriwijaya")
            maskapai = int(input("Pilih nomor maskapai: "))
            pengiriman = PengirimanInternasional(asal, tujuan, maskapai=maskapai)
        else:
            print("Metode tidak valid.")
            continue
    elif internasional == "n":
        if internasional == "n":
            print("1. Darat")
            print("2. Udara")
            metode = int(input("Pilih metode pengiriman: "))
            if metode == 1:
                print("1. Mobil")
                print("2. Truk")
                print("3. Motor")
                jenis_kendaraan = int(input("Jenis kendaraan: "))
                pengiriman = PengirimanDarat(asal, tujuan, jenis_kendaraan)
            elif metode == 2:
                print("1. Air Asia")
                print("2. riwijaya")
                maskapai = int(input("Pilih maskapai: "))
                pengiriman = PengirimanUdara(asal, tujuan, maskapai)
            else:
                print("Metode tidak valid.")
    else:
        print("metode tidak valid")
        continue
    daftar_pengiriman.append(pengiriman)
    ulang = input("Apakah Anda ingin menginputkan ulang? (y/n): ")
    if ulang.lower() == "y":
        continue
    elif ulang.lower() == "n":
        break
    else:
        print("Penginputan tidak valid")
print("\n--- HASIL ESTIMASI PENGIRIMAN ---")
for data in (daftar_pengiriman):
    print(f"- {data.estimasi_waktu()}")

