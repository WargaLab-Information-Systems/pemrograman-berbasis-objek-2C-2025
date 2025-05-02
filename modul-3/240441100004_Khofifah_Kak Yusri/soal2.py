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
            return 7
        elif self.jenis_kendaraan.lower() == "mobil":
            return 5
        else:
            return 6
        
class PengirimanUdara(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        super().__init__(asal, tujuan)
        self.maskapai = maskapai

    def estimasi_waktu(self):
        if self.maskapai.lower() == "garuda":
            return 2
        elif self.maskapai.lower() == "lion air":
            return 3
        else:
            return 4

class PengirimanInternasional(Pengiriman):
    def __init__(self, asal, tujuan, jenis_kendaraan, maskapai):
        super().__init__(asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan
        self.maskapai = maskapai

    def estimasi_waktu(self):
        if self.jenis_kendaraan.lower() == "truk":
            waktu_darat = 7
        elif self.jenis_kendaraan.lower() == "mobil":
            waktu_darat = 5
        else:
            waktu_darat = 6

        if self.maskapai.lower() == "garuda":
            waktu_udara = 2
        elif self.maskapai.lower() == "lion air":
            waktu_udara = 3
        else:
            waktu_udara = 4

        waktu_tercepat = min(waktu_darat, waktu_udara)

        if self.tujuan.lower() != "indonesia":
            waktu_tercepat += 3

        return waktu_tercepat

pengiriman1 = PengirimanInternasional("Jakarta", "Malaysia", "Truk", "Garuda")
pengiriman2 = PengirimanInternasional("Surabaya", "Indonesia", "Mobil", "Lion Air")
pengiriman3 = PengirimanInternasional("Bandung", "Singapura", "Motor", "Air Asia")

print(f"Estimasi waktu pengiriman 1: {pengiriman1.estimasi_waktu()} hari")
print(f"Estimasi waktu pengiriman 2: {pengiriman2.estimasi_waktu()} hari")
print(f"Estimasi waktu pengiriman 3: {pengiriman3.estimasi_waktu()} hari")

