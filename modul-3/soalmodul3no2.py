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
            return 7 
        elif self.jenis_kendaraan == "truk":
            return 10 
        else:
            return super().estimasi_waktu()

class PengirimanUdara(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        super().__init__(asal, tujuan)
        self.maskapai = maskapai
    
    def estimasi_waktu(self):
        if self.maskapai == "Garuda":
            return 3 
        elif self.maskapai == "Lion Air":
            return 4 
        else:
            return super().estimasi_waktu()

class PengirimanInternasional(Pengiriman):
    def __init__(self, asal, tujuan, jenis_kendaraan=None, maskapai=None):
        Pengiriman.__init__(self, asal, tujuan)
        self.pengiriman_darat = PengirimanDarat(asal, tujuan, jenis_kendaraan)
        self.pengiriman_udara = PengirimanUdara(asal, tujuan, maskapai)
    
    def estimasi_waktu(self):
        if "luar negeri" in self.tujuan.lower():  
            estimasi_darat = self.pengiriman_darat.estimasi_waktu()
            estimasi_udara = self.pengiriman_udara.estimasi_waktu()
            estimasi = max(estimasi_darat, estimasi_udara)
            return estimasi + 3  
        else:
            estimasi_darat = self.pengiriman_darat.estimasi_waktu()
            estimasi_udara = self.pengiriman_udara.estimasi_waktu()
            return max(estimasi_darat, estimasi_udara)

pengiriman1 = PengirimanInternasional("Jakarta", "New York", jenis_kendaraan="mobil", maskapai="Garuda")
pengiriman2 = PengirimanInternasional("Bandung", "Paris", jenis_kendaraan="truk", maskapai="Lion Air")
pengiriman3 = PengirimanInternasional("Surabaya", "Singapore", jenis_kendaraan="mobil", maskapai="Lion Air")

print(f"Estimasi waktu pengiriman 1: {pengiriman1.estimasi_waktu()} hari")
print(f"Estimasi waktu pengiriman 2: {pengiriman2.estimasi_waktu()} hari")
print(f"Estimasi waktu pengiriman 3: {pengiriman3.estimasi_waktu()} hari")
