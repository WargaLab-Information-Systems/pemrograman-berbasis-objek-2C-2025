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
            return 3
        elif self.jenis_kendaraan == "truk":
            return 7
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
        estimasi_darat = PengirimanDarat(self.asal, self.tujuan, self.jenis_kendaraan).estimasi_waktu()
        estimasi_udara = PengirimanUdara(self.asal, self.tujuan, self.maskapai).estimasi_waktu()
        estimasi = (estimasi_darat + estimasi_udara)

        if self.tujuan != "Indonesia":
            estimasi += 3

        return estimasi

    def info_estimasi(self):
        waktu = self.estimasi_waktu()
        if self.tujuan != "Indonesia":
            return f"{waktu} hari (pengiriman internasional – termasuk tambahan 3 hari)"
        else:
            return f"{waktu} hari (pengiriman dalam negeri)"

pengiriman1 = PengirimanInternasional("Jakarta", "Singapura", "mobil", "Garuda")
pengiriman2 = PengirimanInternasional("Bandung", "USA", "truk", "AirAsia")
pengiriman3 = PengirimanInternasional("Surabaya", "Indonesia", "mobil", "Garuda")

print("Estimasi Pengiriman 1:", pengiriman1.info_estimasi())
print("Estimasi Pengiriman 2:", pengiriman2.info_estimasi())
print("Estimasi Pengiriman 3:", pengiriman3.info_estimasi())
