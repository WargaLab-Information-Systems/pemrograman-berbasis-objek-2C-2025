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
        if self.jenis_kendaraan.lower() == "truk":
            return 2
        elif self.jenis_kendaraan.lower() == "mobil":
            return 3
        else:
            return 0  


class PengirimanUdara(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        super().__init__(asal, tujuan)
        self.maskapai = maskapai

    def estimasi_waktu(self):
        if self.maskapai.lower() == "garuda":
            return 2
        elif self.maskapai.lower() == "sriwijaya":
            return 3
        else:
            return 0


class PengirimanInternasional(PengirimanDarat, PengirimanUdara):
    def __init__(self, asal, tujuan, metode_pengiriman, jenis_kendaraan=None, maskapai=None):
        self.metode_pengiriman = metode_pengiriman
        self.asal = asal
        self.tujuan = tujuan
        if metode_pengiriman == 'udara':
            self.maskapai = maskapai
        else:
            self.jenis_kendaraan = jenis_kendaraan

    def estimasi_waktu(self):
        if self.metode_pengiriman == 'udara':
            waktu_dasar = PengirimanUdara.estimasi_waktu(self)
            metode = "Pengiriman Udara"
            transportasi = self.maskapai
        else:
            waktu_dasar = PengirimanDarat.estimasi_waktu(self)
            metode = "Pengiriman Darat"
            transportasi = self.jenis_kendaraan

        waktu_total = waktu_dasar + 3

        print(f"=== Informasi Pengiriman Internasional ===")
        print()
        print(f"Asal              : {self.asal}")
        print(f"Tujuan            : {self.tujuan}")
        print(f"Metode Pengiriman : {metode}")
        print(f"Transportasi      : {transportasi}")
        print(f"Estimasi Waktu    : {waktu_total} hari")
        print()


shipment1 = PengirimanInternasional("Surabaya", "Shanghai", "udara", maskapai="garuda")
shipment1.estimasi_waktu()

shipment2 = PengirimanInternasional("Batam", "Kuala Lumpur", "darat", jenis_kendaraan="truk")
shipment2.estimasi_waktu()

shipment3 = PengirimanInternasional("Jakarta", "Singapura", "udara", maskapai="sriwijaya")
shipment3.estimasi_waktu()
