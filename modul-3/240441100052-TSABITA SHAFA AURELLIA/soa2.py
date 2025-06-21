
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
        if self.jenis_kendaraan == "truk":
            return 6
        elif self.jenis_kendaraan == "motor":
            return 4
        else:
            return super().estimasi_waktu()


class PengirimanUdara(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        super().__init__(asal, tujuan)
        self.maskapai = maskapai

    def estimasi_waktu(self):
        if self.maskapai == "Garuda":
            return 2
        elif self.maskapai == "AirAsia":
            return 3
        else:
            return super().estimasi_waktu()

class PengirimanInternasional(PengirimanDarat, PengirimanUdara):
    def __init__(self, asal, tujuan, jenis_kendaraan, maskapai):
        Pengiriman.__init__(self, asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan
        self.maskapai = maskapai

    def estimasi_waktu(self):
        waktu_darat = PengirimanDarat.estimasi_waktu(self)
        waktu_udara = PengirimanUdara.estimasi_waktu(self)
        estimasi_awal = min(waktu_darat, waktu_udara)

       
        tujuan_dalam_negeri = ["Jakarta", "Bandung", "Surabaya"]
        if self.tujuan not in tujuan_dalam_negeri:
            return estimasi_awal + 3
        else:
            return estimasi_awal


peng1 = PengirimanInternasional("Jakarta", "Singapura", "truk", "Garuda")
peng2 = PengirimanInternasional("Bandung", "Tokyo", "motor", "AirAsia")
peng3 = PengirimanInternasional("Surabaya", "Jakarta", "motor", "Lion")

print(f"Estimasi pengiriman 1: {peng1.estimasi_waktu()} hari")
print(f"Estimasi pengiriman 2: {peng2.estimasi_waktu()} hari")
print(f"Estimasi pengiriman 3: {peng3.estimasi_waktu()} hari")
