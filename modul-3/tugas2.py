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
        if self.jenis_kendaraan.lower() == 'truk':
            return 7
        elif self.jenis_kendaraan.lower() == 'motor':
            return 4
        else:
            return 6  

class PengirimanUdara(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        super().__init__(asal, tujuan)
        self.maskapai = maskapai

    def estimasi_waktu(self):
        if self.maskapai.lower() == 'garuda':
            return 2
        elif self.maskapai.lower() == 'lion air':
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
        waktu = min(waktu_darat, waktu_udara)

        if self.tujuan.lower() != 'indonesia':
            waktu += 3 

        return waktu

pengiriman1 = PengirimanInternasional("Jakarta", "Singapura", "Truk", "garuda")
pengiriman2 = PengirimanInternasional("Surabaya", "Indonesia", "Motor", "lion air")
pengiriman3 = PengirimanInternasional("Bandung", "Malaysia", "Mobil", "AirAsia")

print(f"Estimasi waktu pengiriman 1: {pengiriman1.estimasi_waktu()} hari")
print(f"Estimasi waktu pengiriman 2: {pengiriman2.estimasi_waktu()} hari")
print(f"Estimasi waktu pengiriman 3: {pengiriman3.estimasi_waktu()} hari")
