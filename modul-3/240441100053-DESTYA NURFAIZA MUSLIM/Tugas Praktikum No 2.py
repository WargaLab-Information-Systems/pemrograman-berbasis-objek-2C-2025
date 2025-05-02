class Pengiriman:
    def __init__(self, asal, tujuan):
        self.asal = asal
        self.tujuan = tujuan
    
    def estimasi_waktu(self):
        return 2
    
class PengirimanDarat(Pengiriman):
    def __init__(self, asal, tujuan, jenis_kendaraan):
        super().__init__(asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan
        
    def estimasi_waktu(self):
        if self.jenis_kendaraan == "Truk":
            return 6
        elif self.jenis_kendaraan == "Mobil Box":
            return 5
        elif self.jenis_kendaraan == "Motor":
            return 3
        else:
            return 10
    
class PengirimanUdara(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        super().__init__(asal, tujuan)
        self.maskapai = maskapai

    def estimasi_waktu(self):
        if self.maskapai == "Garuda":
            return 1
        elif self.maskapai == "Lion Air":
            return 3
        elif self.maskapai == "Air Asia":
            return 2
        else:
            return 10
    
class PengirimanInternasional:
    def __init__(self, asal, tujuan, jenis_kendaraan, maskapai):
        self.darat = PengirimanDarat(asal, tujuan, jenis_kendaraan)
        self.udara = PengirimanUdara(asal, tujuan, maskapai)

    def estimasi_waktu(self):
        waktu_darat = self.darat.estimasi_waktu()
        waktu_udara = self.udara.estimasi_waktu()
        estimasi = min(waktu_darat, waktu_udara)

        tujuan = self.darat.tujuan 
        if tujuan != "Indonesia":
            estimasi += 3

        return estimasi

p1 = PengirimanDarat("Jakarta Timur", "Gresik", "Mobil Box")
p2 = PengirimanUdara("Bali", "Palembang", "Garuda")
p3 = PengirimanInternasional("Norwegia", "Singapura", "Truk", "Air Asia")

print(f"Estimasi Pengiriman 1 : {p1.estimasi_waktu()} hari")
print(f"Estimasi Pengiriman 2 : {p2.estimasi_waktu()} hari")
print(f"Estimasi Pengiriman 3 : {p3.estimasi_waktu()} hari")
