class Pengiriman:
    def __init__(self, asal, tujuan):
        self.asal = asal
        self.tujuan = tujuan

    def estimasi_waktu(self):
        if self.asal.lower() == self.tujuan.lower():
            return 1 
        else:
            return 3  

class PengirimanDarat(Pengiriman):
    def __init__(self, asal, tujuan, jenis_kendaraan):
        super().__init__(asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan

    def estimasi_darat(self):
        if self.jenis_kendaraan.lower() == "truk":
            return 4
        elif self.jenis_kendaraan.lower() == "motor":
            return 2
        else:
            return 3

class PengirimanUdara(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        super().__init__(asal, tujuan)
        self.maskapai = maskapai

    def estimasi_udara(self):
        if self.maskapai.lower() == "garuda":
            return 1
        else:
            return 2

class PengirimanInternasional(PengirimanDarat, PengirimanUdara):
    def __init__(self, asal, tujuan, jenis_kendaraan, maskapai):
        Pengiriman.__init__(self, asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan
        self.maskapai = maskapai

    def estimasi_waktu(self):
        estimasi_waktu = Pengiriman.estimasi_waktu(self)
        waktu_darat = PengirimanDarat.estimasi_darat(self)
        waktu_udara = PengirimanUdara.estimasi_udara(self)

        total = estimasi_waktu + waktu_darat + waktu_udara
        return total


p1 = PengirimanInternasional("Jakarta", "Tokyo", "truk", "Garuda")    
p2 = PengirimanInternasional("Surabaya", "Jepang", "motor", "AirAsia") 
p3 = PengirimanInternasional("Bandung", "Bandung", "mobil", "Lion")    

print(f"Asal: {p1.asal}, Tujuan: {p1.tujuan}, Jenis Kendaraan: {p1.jenis_kendaraan}, Maskapai: {p1.maskapai}, Estimasi: {p1.estimasi_waktu()} hari")
print(f"Asal: {p2.asal}, Tujuan: {p2.tujuan}, Jenis Kendaraan: {p2.jenis_kendaraan}, Maskapai: {p2.maskapai}, Estimasi: {p2.estimasi_waktu()} hari")
print(f"Asal: {p3.asal}, Tujuan: {p3.tujuan}, Jenis Kendaraan: {p3.jenis_kendaraan}, Maskapai: {p3.maskapai}, Estimasi: {p3.estimasi_waktu()} hari")