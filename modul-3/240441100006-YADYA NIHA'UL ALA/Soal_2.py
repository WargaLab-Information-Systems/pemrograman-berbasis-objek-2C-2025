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
        super().estimasi_waktu()
        if self.jenis_kendaraan.lower() == "truck":
            return 3
        if self.jenis_kendaraan.lower() == "motor":
            return 1
        if self.jenis_kendaraan.lower() == "mobil":
            return 2
        else :
            return 5
    
    def info(self):
        print(f"\n[Ni Hao Cargo - Pengiriman Darat] Dari {self.asal} ke {self.tujuan}")
        print(f"Jenis kendaraan: {self.jenis_kendaraan}")
        print(f"Estimasi waktu: {self.estimasi_waktu()} hari")

class PengirimanUdara(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        super().__init__(asal, tujuan)
        self.maskapai = maskapai
    
    def estimasi_waktu(self):
        super().estimasi_waktu()
        if self.maskapai.lower() == "Air Hong Kong":
            return 9
        elif self.maskapai.lower() == "Star Cargo":
            return 12
        else :
            return 6

    def info(self):
        print(f"\n[Ni Hao Cargo - Pengiriman Udara] Dari {self.asal} ke {self.tujuan}")
        print(f"Maskapai: {self.maskapai}")
        print(f"Estimasi waktu: {self.estimasi_waktu()} hari")
    
class PengirimanInternasional(PengirimanDarat, PengirimanUdara):
    def __init__(self, asal, tujuan, jenis_kendaraan, maskapai):
        Pengiriman.__init__(self, asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan
        self.maskapai = maskapai

    def estimasi_waktu(self):
        super().estimasi_waktu()
        waktu_darat = PengirimanDarat.estimasi_waktu(self)
        waktu_udara = PengirimanUdara.estimasi_waktu(self)
        total = waktu_darat + waktu_udara
        if self.tujuan != "Indonesia":
            total += 3
        return total
    
    def info(self):
        print(f"\n[Ni Hao Cargo - Pengiriman Internasional]")
        print(f"Dari {self.asal} ke {self.tujuan}")
        print(f"Jenis kendaraan: {self.jenis_kendaraan}")
        print(f"Maskapai: {self.maskapai}")
        print(f"Estimasi waktu: {self.estimasi_waktu()} hari")

paket1 = PengirimanInternasional("Indonesia", "Malaysia", "Truck", "Air Hong Kong")
paket1.info()      

paket2 = PengirimanInternasional("Indonesia", "Indonesia", "Mobil", "Star Cargo")
paket2.info() 

paket3 = PengirimanInternasional("Indonesia", "China", "Truck", "Air Hong Kong")
paket3.info() 

# paket2 = PengirimanDarat("Jawa Timur", "Jawa Tengah", "Mobil")  
# paket2.info()

# paket3 = PengirimanUdara("Indonesia", "Malaysia", "Star Cargo")
# paket3.info()