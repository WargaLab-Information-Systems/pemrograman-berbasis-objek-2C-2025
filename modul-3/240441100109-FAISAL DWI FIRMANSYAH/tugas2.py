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
            return 4
        elif self.jenis_kendaraan == "Motor":
            return 3
        else:
            return 5

class PengirimanUdara(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        super().__init__(asal, tujuan)
        self.maskapai = maskapai

    def estimasi_waktu(self):
        if self.maskapai == "Super Air Jet":
            return 1
        elif self.maskapai == "Lion Air":
            return 2
        elif self.maskapai == "AirAsia":
            return 3
        else:
            return 4  

class PengirimanInternasional(PengirimanDarat, PengirimanUdara):
    def __init__(self, asal, tujuan, jenis_kendaraan, maskapai):
        Pengiriman.__init__(self, asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan
        self.maskapai = maskapai

    def estimasi_waktu(self):
        if self.maskapai == "Super Air Jet":
            waktu = 1
        elif self.maskapai == "Lion Air":
            waktu = 2
        elif self.maskapai == "AirAsia":
            waktu = 3
        else:
            waktu = 4

        if self.tujuan != "Indonesia":
            return waktu + 3
        else:
            return waktu

    def tampilkan_info(self, nomor):
        print(f"Pengiriman Barang ke-{nomor}:")
        print(f"  Asal          : {self.asal}")
        print(f"  Tujuan        : {self.tujuan}")
        print(f"  Kendaraan     : {self.jenis_kendaraan}")
        print(f"  Maskapai      : {self.maskapai}")
        print(f"  Estimasi Hari : {self.estimasi_waktu()} hari\n")

daftar_pengiriman = [
    PengirimanInternasional("Jakarta", "Jepang", "Truk", "Super Air Jet"),
    PengirimanInternasional("Surabaya", "Indonesia", "Motor", "Lion Air"),
    PengirimanInternasional("Medan", "Malaysia", "Truk", "AirAsia"),
    PengirimanInternasional("Bandung", "Thailand", "Motor", "Garuda"),
    PengirimanInternasional("Yogyakarta", "Indonesia", "Truk", "Super Air Jet"),
]

for i, pengiriman in enumerate(daftar_pengiriman, start=1):
    pengiriman.tampilkan_info(i)