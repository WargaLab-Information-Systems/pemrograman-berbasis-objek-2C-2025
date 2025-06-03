class Pengiriman:
    def __init__(self, asal, tujuan):
        self.asal = asal
        self.tujuan = tujuan

    def estimasi_waktu(self):
        return 5  

    def info(self):
        print("Asal               :", self.asal)
        print("Tujuan             :", self.tujuan)
        print("Estimasi Waktu     :", self.estimasi_waktu(), "hari")


class PengirimanDarat(Pengiriman):
    def __init__(self, asal, tujuan, jenis_kendaraan):
        super().__init__(asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan

    def estimasi_waktu(self):
        if self.jenis_kendaraan == "truk":
            return 7
        elif self.jenis_kendaraan == "mobil":
            return 5
        elif self.jenis_kendaraan == "motor":
            return 4
        else:
            return super().estimasi_waktu()

    def info(self):
        print("Asal               :", self.asal)
        print("Tujuan             :", self.tujuan)
        print("Estimasi Waktu     :", self.estimasi_waktu(), "hari")
        print("Jenis Kendaraan    :", self.jenis_kendaraan)
        print("-" * 40)


class PengirimanUdara(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        super().__init__(asal, tujuan)
        self.maskapai = maskapai

    def estimasi_waktu(self):
        if self.maskapai == "garuda":
            return 2
        elif self.maskapai in ["lion air", "lion"]:
            return 3
        elif self.maskapai == "airasia":
            return 4
        else:
            return super().estimasi_waktu()

    def info(self):
        print("Asal               :", self.asal)
        print("Tujuan             :", self.tujuan)
        print("Estimasi Waktu     :", self.estimasi_waktu(), "hari")
        print("Maskapai           :", self.maskapai)
        print("-" * 40)


class PengirimanInternasional(PengirimanDarat, PengirimanUdara):
    def __init__(self, asal, tujuan, jenis_kendaraan, maskapai):
        Pengiriman.__init__(self, asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan
        self.maskapai = maskapai

    def estimasi_waktu(self):
        darat = PengirimanDarat(self.asal, self.tujuan, self.jenis_kendaraan).estimasi_waktu()
        udara = PengirimanUdara(self.asal, self.tujuan, self.maskapai).estimasi_waktu()
        estimasi = (darat + udara)

        if self.tujuan != "indonesia":
            estimasi += 3

        return estimasi

    def info(self):
        print("Asal               :", self.asal)
        print("Tujuan             :", self.tujuan)
        print("Jenis Kendaraan    :", self.jenis_kendaraan)
        print("Maskapai           :", self.maskapai)
        print("Estimasi Waktu     :", self.estimasi_waktu(), "hari")
        print("-" * 40)


pengiriman1 = PengirimanInternasional("Jakarta", "Thailand", "truk", "Garuda")
pengiriman2 = PengirimanUdara("Surabaya", "Bali", "Lion Air")
pengiriman3 = PengirimanDarat("Bandung", "Jogjakarta", "mobil")

pengiriman1.info()
pengiriman2.info()
pengiriman3.info()
