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
        estimasi = estimasi_darat + estimasi_udara

        if self.tujuan.lower() != "indonesia":
            estimasi += 3

        return estimasi

    def info_pengiriman(self):
        print("===== Informasi Pengiriman =====")
        print(f"Asal               : {self.asal}")
        print(f"Tujuan             : {self.tujuan}")
        print(f"Jenis Kendaraan    : {self.jenis_kendaraan}")
        print(f"Maskapai           : {self.maskapai}")
        print(f"Estimasi Waktu     : {self.estimasi_waktu()} hari")
        print("================================\n")



pengiriman1 = PengirimanInternasional("Jakarta", "Singapura", "mobil", "Garuda")
pengiriman2 = PengirimanInternasional("Bandung", "USA", "truk", "AirAsia")
pengiriman3 = PengirimanInternasional("Surabaya", "Indonesia", "mobil", "Garuda")

pengiriman1.info_pengiriman()
pengiriman2.info_pengiriman()
pengiriman3.info_pengiriman()
