class Pengiriman:
    def __init__(self, asal, tujuan):
        self.asal = asal
        self.tujuan = tujuan

    def estimasi_waktu(self):
        return 6

class PengirimanDarat(Pengiriman):
    def __init__(self, asal, tujuan, jenis_kendaraan):
        super().__init__(asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan

    def estimasi_waktu(self):
        if self.jenis_kendaraan == "mobil":
            return 5
        elif self.jenis_kendaraan == "truk":
            return 7
        else:
            return 10

class PengirimanUdara(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        super().__init__(asal, tujuan)
        self.maskapai = maskapai

    def estimasi_waktu(self):
        if self.maskapai == "Maskapai A":
            return 2
        elif self.maskapai == "Maskapai B":
            return 3
        else:
            return 4

class PengirimanInternasional(PengirimanDarat, PengirimanUdara):
    def __init__(self, asal, tujuan, jenis_kendaraan, maskapai):
        Pengiriman.__init__(self, asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan
        self.maskapai = maskapai

    def estimasi_waktu(self):
        waktu_darat = PengirimanDarat.estimasi_waktu(self)
        waktu_udara = PengirimanUdara.estimasi_waktu(self)
        estimasi_awal = max(waktu_darat, waktu_udara)

        if self.tujuan not in ["Jakarta", "Bandung", "Surabaya", "Medan"]:
            estimasi_awal += 3

        return f"Estimasi waktu pengiriman internasional: {estimasi_awal} hari"

pengiriman1 = PengirimanInternasional("Jakarta", "Amerika", "mobil", "Maskapai A")
pengiriman2 = PengirimanInternasional("Bandung", "New York", "truk", "Maskapai B")
pengiriman3 = PengirimanInternasional("Surabaya", "London", "motor", "Maskapai C")

print(pengiriman1.estimasi_waktu())
print(pengiriman2.estimasi_waktu())
print(pengiriman3.estimasi_waktu())