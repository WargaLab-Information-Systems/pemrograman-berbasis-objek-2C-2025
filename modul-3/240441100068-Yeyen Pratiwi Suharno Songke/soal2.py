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
        if self.jenis_kendaraan == "motor":
            return 6
        elif self.jenis_kendaraan == "mobil":
            return 4
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
        elif self.maskapai == "Lion":
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
        waktu_tercepat = (waktu_darat + waktu_udara)
        if self.tujuan != "Indonesia":
            waktu_tercepat += 3
        return waktu_tercepat

pengiriman1 = PengirimanInternasional("Jakarta", "Malaysia", "mobil", "Garuda")
pengiriman2 = PengirimanInternasional("Makassar", "Indonesia", "truk", "Lion")
pengiriman3 = PengirimanInternasional("Surabaya", "Singapura", "motor", "Lion")
pengiriman4 = PengirimanInternasional("Medan", "Indonesia", "mobil", "Citilink")  

print(f"Pengiriman 1 dari {pengiriman1.asal} ke {pengiriman1.tujuan}, kendaraan: {pengiriman1.jenis_kendaraan}, maskapai: {pengiriman1.maskapai} → {pengiriman1.estimasi_waktu()} hari")
print(f"Pengiriman 2 dari {pengiriman2.asal} ke {pengiriman2.tujuan}, kendaraan: {pengiriman2.jenis_kendaraan}, maskapai: {pengiriman2.maskapai} → {pengiriman2.estimasi_waktu()} hari")
print(f"Pengiriman 3 dari {pengiriman3.asal} ke {pengiriman3.tujuan}, kendaraan: {pengiriman3.jenis_kendaraan}, maskapai: {pengiriman3.maskapai} → {pengiriman3.estimasi_waktu()} hari")
print(f"Pengiriman 4 dari {pengiriman4.asal} ke {pengiriman4.tujuan}, kendaraan: {pengiriman4.jenis_kendaraan}, maskapai: {pengiriman4.maskapai} → {pengiriman4.estimasi_waktu()} hari")
