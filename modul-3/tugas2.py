class Pengiriman:
    def __init__(self, asal, tujuan, **kwargs):
        self.asal = asal
        self.tujuan = tujuan
        self.maskapai = kwargs.get('maskapai', None)
        self.jenis_kendaraan = kwargs.get('jenis_kendaraan', None)

    def estimasi_waktu(self):
        return 7  


class PengirimanDarat(Pengiriman):
    def __init__(self, asal, tujuan, **kwargs):
        super().__init__(asal, tujuan, **kwargs)  

    def estimasi_waktu(self):
        waktu = super().estimasi_waktu()
        if self.jenis_kendaraan == "truk":
            waktu = 7  
        elif self.jenis_kendaraan == "mobil":
            waktu = 5 
        else:
            waktu = 6  
        return waktu


class PengirimanUdara(Pengiriman):
    def __init__(self, asal, tujuan, **kwargs):
        super().__init__(asal, tujuan, **kwargs)  

    def estimasi_waktu(self):
        waktu = super().estimasi_waktu()
        if self.maskapai == "Garuda":
            waktu = 3  
        elif self.maskapai == "AirAsia":
            waktu = 4 
        else:
            waktu = 5  
        return waktu


class PengirimanInternasional(PengirimanDarat, PengirimanUdara):
    def __init__(self, asal, tujuan, **kwargs):
        super().__init__(asal, tujuan, **kwargs)  

    def estimasi_waktu(self):
        waktu = super().estimasi_waktu() 
        if "luar negeri" in self.tujuan.lower():
            waktu += 3  
        return f"{waktu} hari"

    def informasi_pengiriman(self):
        info = f"Pengiriman dari {self.asal} ke {self.tujuan}."
        if self.jenis_kendaraan:
            info += f" Jenis kendaraan: {self.jenis_kendaraan}."
        if self.maskapai:
            info += f" Maskapai: {self.maskapai}."
        return info


pengiriman1 = PengirimanInternasional("Gorontalo", "Norwegia", jenis_kendaraan="truk")
pengiriman2 = PengirimanInternasional("Pekanbaru", "Thailand", jenis_kendaraan="mobil")
pengiriman3 = PengirimanInternasional("Bengkulu", "Malaysia", maskapai="Garuda")
pengiriman4 = PengirimanInternasional("Pekanbaru", "Jakarta", jenis_kendaraan="truk", maskapai="Garuda")

print(pengiriman1.informasi_pengiriman())
print(f"Estimasi waktu pengiriman 1: {pengiriman1.estimasi_waktu()}")
print(pengiriman2.informasi_pengiriman())
print(f"Estimasi waktu pengiriman 2: {pengiriman2.estimasi_waktu()}")
print(pengiriman3.informasi_pengiriman())
print(f"Estimasi waktu pengiriman 3: {pengiriman3.estimasi_waktu()}")
print(pengiriman4.informasi_pengiriman())
print(f"Estimasi waktu pengiriman 4: {pengiriman4.estimasi_waktu()}")
