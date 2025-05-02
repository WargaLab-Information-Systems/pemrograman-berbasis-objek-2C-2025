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
            return 2
        elif self.jenis_kendaraan == "motor":
            return 4
        else:
            return 5

class PengirimanUdara(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        super().__init__(asal, tujuan)
        self.maskapai = maskapai
    def estimasi_waktu(self):
        if self.maskapai == "Garuda":
            return 2
        else:
            return 3

class PengirimanInternasional(PengirimanDarat, PengirimanUdara):
    def __init__(self, asal, tujuan, jenis_kendaraan, maskapai):
        Pengiriman.__init__(self, asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan
        self.maskapai = maskapai
    def estimasi_waktu(self):
        waktu_darat = PengirimanDarat.estimasi_waktu(self)
        waktu_udara = PengirimanUdara.estimasi_waktu(self)

        waktu = min(waktu_darat, waktu_udara)
        if self.tujuan != self.asal:  
            waktu += 3
        return waktu
    def info_pengiriman(self):
        print(f"Asal: {self.asal:} Tujuan: {self.tujuan:} Kendaraan: {self.jenis_kendaraan:} Maskapai: {self.maskapai:} Estimasi: {self.estimasi_waktu()} hari")

Pengiriman1 = PengirimanInternasional("Surabaya", "Tokyo", "truk", "Garuda")
Pengiriman2 = PengirimanInternasional("Surabaya", "Jepang", "motor", "AirAsia")
pengiriman3 = PengirimanInternasional("Malang", "Malaysia", "mobil", "Lion Air")

Pengiriman1.info_pengiriman()
Pengiriman2.info_pengiriman()
pengiriman3.info_pengiriman()
