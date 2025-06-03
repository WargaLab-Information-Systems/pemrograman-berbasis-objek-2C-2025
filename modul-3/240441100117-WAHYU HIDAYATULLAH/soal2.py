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
        if self.jenis_kendaraan == "Truk":
            return 8
        elif self.jenis_kendaraan == "Motor":
            return 6
        else:
            return super().estimasi_waktu()

class PengirimanUdara(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        super().__init__(asal, tujuan)
        self.maskapai = maskapai

    def estimasi_waktu(self):
        if self.maskapai == "Garuda":
            return 2
        elif self.maskapai == "Batik":
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
        estimasi = min(waktu_darat, waktu_udara)
        if self.tujuan != "indonesia":
            estimasi += 3
        return estimasi
    
    def tampilkan_info(self, nomor):
        print(f"Pengiriman Barang ke-{nomor}: ")
        print(f"Asal          : {self.asal}")
        print(f"Tujuan        : {self.tujuan}")
        print(f"Kendaraan     : {self.jenis_kendaraan}")
        print(f"Maskapai      : {self.maskapai}")
        print(f"Estimasi Hari : {self.estimasi_waktu()} hari\n")

daftar_pengiriman = [
    PengirimanInternasional("Jakarta", "Jepang", "Truk", "Batik"),
    PengirimanInternasional("Sumenep", "indonesia", "Motor", "Lion Air"),
    PengirimanInternasional("Pamekasan", "Malaysia", "Truk", "AirAsia"),
    PengirimanInternasional("Bandung", "Thailand", "Motor", "Garuda"),
    PengirimanInternasional("Yogyakarta", "indonesia", "Truk", "Sriwijaya Air"),
]

for i, pengiriman in enumerate(daftar_pengiriman, start=1):
    pengiriman.tampilkan_info(i)