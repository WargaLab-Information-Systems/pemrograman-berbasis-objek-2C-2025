class Pengiriman:
    def __init__(self, asal, tujuan):
        self.asal = asal
        self.tujuan = tujuan
    def estimasi_waktu(self):
        print("Estimasi waktu pengiriman 12 hari.")
        return 12

class PengirimanDarat(Pengiriman):
    def __init__(self, asal, tujuan, jenis_kendaraan):
        super().__init__(asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan.lower()

    def estimasi_waktu(self):
        if self.jenis_kendaraan == "truck":
            print("Waktu estimasi pengiriman darat adalah 5 hari.")
            return 5
        elif self.jenis_kendaraan == "mobil box" or self.jenis_kendaraan == "mobil pick up":
            print("Waktu estimasi pengiriman darat adalah 6 hari.")
            return 6
        else:
            print("Waktu estimasi pengiriman darat adalah 7 hari.")
            return 7

class PengirimanUdara(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        super().__init__(asal, tujuan)
        self.maskapai = maskapai.lower()

    def estimasi_waktu(self):
        if self.maskapai == "garuda":
            print("Waktu estimasi pengiriman udara adalah 2 hari.")
            return 2
        elif self.maskapai == "citilink" or self.maskapai == "lion air":
            print("Waktu estimasi pengiriman udara adalah 3 hari.")
            return 3
        else:
            print("Waktu estimasi pengiriman udara adalah 5 hari.")
            return 5
        
class PengirimanInternasional(PengirimanDarat, PengirimanUdara):
    def __init__(self, asal, tujuan, jenis_kendaraan, maskapai):
        self.asal = asal
        self.tujuan = tujuan
        self.jenis_kendaraan = jenis_kendaraan.lower()
        self.maskapai = maskapai.lower()
        self.cek_lokasi()

    def cek_lokasi(self):
        self.internasional = self.asal.lower() != self.tujuan.lower()

    def estimasi_waktu(self):
        pengiriman_darat = PengirimanDarat(self.asal, self.tujuan, self.jenis_kendaraan)
        pengiriman_udara = PengirimanUdara(self.asal, self.tujuan, self.maskapai)

        darat = pengiriman_darat.estimasi_waktu()
        udara = pengiriman_udara.estimasi_waktu()

        estimasi = darat + udara

        if self.internasional:
            estimasi += 3
            print("Pengiriman internasional, waktu ditambah 3 hari.")
            print(f"Total estimasi waktu pengiriman internasional dari {self.asal} ke {self.tujuan} adalah {estimasi} hari.")
        else:
            print(f"Total waktu estimasi pengiriman dalam negeri adalah {estimasi} hari.")

paket1 = PengirimanInternasional("Indonesia", "Indonesia", "mobil pick up", "lion air")
paket2 = PengirimanInternasional("Indonesia", "Inggris", "mobil box", "garuda")
paket3 = PengirimanInternasional("Indonesia", "Mesir", "truck", "citilink")
paket4 = PengirimanInternasional("Indonesia", "India", "sepeda motor", "qatar airways")
paket1.estimasi_waktu()
print()
paket2.estimasi_waktu()
print()
paket3.estimasi_waktu()
print()
paket4.estimasi_waktu()