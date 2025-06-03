class Pengiriman:
    def __init__(self, asal, tujuan):
        self.asal = asal
        self.tujuan = tujuan

    def estimasi_waktu(self):
        return 5

class PengirimanInternasional(Pengiriman):
    def __init__(self, asal, tujuan, jenis_kendaraan, maskapai):
        super().__init__(asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan
        self.maskapai = maskapai

    def estimasi_waktu(self):
        # Estimasi berdasarkan kendaraan
        if self.jenis_kendaraan.lower() == "truk":
            waktu_darat = 7
        elif self.jenis_kendaraan.lower() == "motor":
            waktu_darat = 4
        else:
            waktu_darat = 6

        # Estimasi berdasarkan maskapai
        if self.maskapai.lower() == "garuda":
            waktu_udara = 2
        elif self.maskapai.lower() == "airasia":
            waktu_udara = 3
        else:
            waktu_udara = 4

        estimasi_awal = min(waktu_darat, waktu_udara)

        # Tambah 3 hari jika tujuan luar negeri
        if self.tujuan.lower() not in ["jakarta", "surabaya", "bandung"]:
            return estimasi_awal + 3
        else:
            return estimasi_awal

# Contoh penggunaan
penggunaan1 = PengirimanInternasional("Jakarta", "Singapura", "Truk", "Garuda")
penggunaan2 = PengirimanInternasional("Surabaya", "Bandung", "Motor", "AirAsia")
penggunaan3 = PengirimanInternasional("Jakarta", "Malaysia", "Truk", "Lion")

print(f"Pengiriman 1 dari {penggunaan1.asal} ke {penggunaan1.tujuan}: {penggunaan1.estimasi_waktu()} hari")
print(f"Pengiriman 2 dari {penggunaan2.asal} ke {penggunaan2.tujuan}: {penggunaan2.estimasi_waktu()} hari")
print(f"Pengiriman 3 dari {penggunaan3.asal} ke {penggunaan3.tujuan}: {penggunaan3.estimasi_waktu()} hari")