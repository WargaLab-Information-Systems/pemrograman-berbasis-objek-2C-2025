class Pengiriman:
    def __init__(self, asal, tujuan):
        self.asal = asal
        self.tujuan = tujuan
        
    def waktu_pengiriman(self):
        return 5

class Darat(Pengiriman):
    def __init__(self, asal, tujuan, kendaraan):
        super().__init__(asal, tujuan)
        self.kendaraan = kendaraan
        
    def waktu_pengiriman(self):
        if self.kendaraan == "1":
            return 3
        elif self.kendaraan == "2":
            return 4
        elif self.kendaraan == "3":
            return 7
        else:
            print("Tidak ada pilihan kendaraan")
            return 0

class Udara(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        super().__init__(asal, tujuan)
        self.maskapai = maskapai
        
    def waktu_pengiriman(self):
        if self.maskapai == "1":
            return 1
        elif self.maskapai == "2":
            return 2
        else:
            print("Tidak ada pilihan maskapai")
            return 0

class Internasional(Darat, Udara):
    def __init__(self, asal, tujuan, kendaraan, maskapai, metode):
        self.asal = asal
        self.tujuan = tujuan
        self.kendaraan = kendaraan
        self.maskapai = maskapai
        self.metode = metode
        
    def waktu_pengiriman(self):
        waktu = 0
        tujuan_dalam_negeri = ["indonesia", "surabaya", "bandung", "gresik", "lamongan", 
                               "kediri", "jombang", "jogja", "bali", "lumajang", "malang", 
                               "pasuruan","jakarta","madura","sidoarja","jember","ponorogo",
                               "probolinggo","pandaan","bekasi","medan","tuban"]
        
        if self.metode == "darat":
            waktu = Darat.waktu_pengiriman(self)
        elif self.metode == "udara":
            waktu = Udara.waktu_pengiriman(self)
        elif self.metode == "gabungan":
            waktu = Darat.waktu_pengiriman(self) + Udara.waktu_pengiriman(self)
        else:
            waktu = 0

        if self.tujuan.lower() not in tujuan_dalam_negeri:
            waktu += 3

        return waktu

print("\n==Pengiriman==")
asal = input("Masukkan asal pengiriman: ")
tujuan = input("Masukkan tujuan pengiriman (dalam/luar negeri): ")

while True:
    print("\nPilih jenis kendaraan:")
    print("1. Motor")
    print("2. Mobil")
    print("3. Truk")
    kendaraan = input("Masukkan pilihan kendaraan (1/2/3): ")
    if kendaraan in ["1", "2", "3"]:
        break
    else:
        print("Tidak ada dalam pilihan")

while True:
    print("\nPilih maskapai:")
    print("1. Garuda")
    print("2. Lion Air")
    maskapai = input("Masukkan pilihan maskapai (1/2): ")
    if maskapai in ["1", "2"]:
        break
    else:
        print("Tidak ada pilihan")

while True:
    print("\nPilih metode pengiriman:")
    print("darat / udara / gabungan")
    metode = input("Masukkan metode: ").lower()
    if metode in ["darat", "udara", "gabungan"]:
        break
    else:
        print("Metode tidak tersedia")

pengiriman = Internasional(asal, tujuan, kendaraan, maskapai, metode)
print(f"\nEstimasi waktu pengiriman: {pengiriman.waktu_pengiriman()} hari")