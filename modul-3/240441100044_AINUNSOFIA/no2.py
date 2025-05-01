# Class induk
class Pengiriman:
    def __init__(self, asal, tujuan): #constructor
        self.asal = asal
        self.tujuan = tujuan

    def estimasi_waktu(self):
        return 5  # default estimasi 5 hari


# Class turunan untuk Pengiriman Darat
class PengirimanDarat(Pengiriman):
    def __init__(self, asal, tujuan, jenis_kendaraan):
        super().__init__(asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan

    def estimasi_waktu(self):
        if self.jenis_kendaraan == "Mobil":
            return 6  # Mobil butuh 6 hari
        elif self.jenis_kendaraan == "Motor":
            return 4  # Motor lebih cepat 4 hari
        else:
            return super().estimasi_waktu()  # Default ke 5 hari


# Class turunan untuk Pengiriman Udara
class PengirimanUdara(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        super().__init__(asal, tujuan)
        self.maskapai = maskapai

    def estimasi_waktu(self):
        if self.maskapai == "Garuda":
            return 2  # Garuda lebih cepat 2 hari
        elif self.maskapai == "Lion Air":
            return 3  # Lion Air 3 hari
        else:
            return super().estimasi_waktu()


# Class turunan Internasional dari Darat dan Udara
class PengirimanInternasional(PengirimanDarat, PengirimanUdara):
    def __init__(self, asal, tujuan, jenis_kendaraan, maskapai):
        Pengiriman.__init__(self, asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan
        self.maskapai = maskapai

    def estimasi_waktu(self):
        waktu_udara = PengirimanUdara.estimasi_waktu(self)
        if self.tujuan not in ["Jakarta", "Surabaya", "Bandung"]:  
            return waktu_udara + 3
        else:
            return waktu_udara


# Membuat beberapa objek
pengiriman1 = PengirimanInternasional("Jakarta", "Singapura", "Mobil", "Garuda")
pengiriman2 = PengirimanInternasional("Jakarta", "Surabaya", "Motor", "Lion Air")
pengiriman3 = PengirimanInternasional("Medan", "Malaysia", "Motor", "Garuda")

# Menampilkan estimasi waktu
print(f"Pengiriman 1 estimasi waktu: {pengiriman1.estimasi_waktu()} hari")
print(f"Pengiriman 2 estimasi waktu: {pengiriman2.estimasi_waktu()} hari")
print(f"Pengiriman 3 estimasi waktu: {pengiriman3.estimasi_waktu()} hari")
