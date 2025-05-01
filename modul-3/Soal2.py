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
        if self.jenis_kendaraan.lower() == "motor":
            return 3
        elif self.jenis_kendaraan.lower() == "mobil":
            return 4
        else:
            return super().estimasi_waktu()

class PengirimanUdara(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        super().__init__(asal, tujuan)
        self.maskapai = maskapai

    def estimasi_waktu(self):
        if self.maskapai.lower() == "garuda":
            return 1
        else:
            return 2

class PengirimanInternasional(Pengiriman):
    def __init__(self, asal, tujuan, jenis_kendaraan, maskapai):
        super().__init__(asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan
        self.maskapai = maskapai

    def estimasi_waktu(self):
        waktu_darat = PengirimanDarat(self.asal, self.tujuan, self.jenis_kendaraan).estimasi_waktu()
        waktu_udara = PengirimanUdara(self.asal, self.tujuan, self.maskapai).estimasi_waktu()
        waktu_tercepat = (waktu_darat + waktu_udara)
 
        if self.asal.lower() != self.tujuan.lower():
            return waktu_tercepat + 3
        else:
            return waktu_tercepat
        
    def info_pengiriman(self):
        print("=== Informasi Pengiriman ===")
        print(f"Asal      : {self.asal}")
        print(f"Tujuan    : {self.tujuan}")
        print(f"Kendaraan : {self.jenis_kendaraan}")
        print(f"Maskapai  : {self.maskapai}")
        print(f"estimasi  : {self.estimasi_waktu()} hari")
        print("-" * 30)
        
pengiriman1 = PengirimanInternasional("Indonesia", "Rusia", "mobil", "Garuda")
pengiriman2 = PengirimanInternasional("Indonesia", "Indonesia", "motor", "Airline")
pengiriman3 = PengirimanInternasional("Indonesia", "Jerman", "motor", "Garuda")
pengiriman4 = PengirimanInternasional("Indonesia", "Indonesia", "mobil", "Airline")

pengiriman1.info_pengiriman()
pengiriman2.info_pengiriman()
pengiriman3.info_pengiriman()
pengiriman4.info_pengiriman()