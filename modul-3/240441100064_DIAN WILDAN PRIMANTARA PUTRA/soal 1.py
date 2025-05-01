class Karyawan:
    def __init__(self, nama, gaji, departemen):
        self.nama = nama
        self.gaji = gaji
        self.departemen = departemen

    def info(self):
        print(f"Nama: {self.nama}")
        print(f"Gaji: {self.gaji}")
        print(f"Departemen: {self.departemen}")

class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji, departemen, tunjangan):
        super().__init__(nama, gaji, departemen)
        self.tunjangan = tunjangan

    def info(self):
        print("Jenis Karyawan: Karyawan Tetap")
        super().info()
        print(f"Tunjangan: {self.tunjangan}")

class KaryawanHarian(Karyawan):
    def __init__(self, nama, gaji, departemen, jam_kerja):
        super().__init__(nama, gaji, departemen)
        self.jam_kerja = jam_kerja

    def info(self):
        print("Jenis Karyawan: Karyawan Harian")
        super().info()
        print(f"Jam Kerja: {self.jam_kerja} jam/hari")

class ManajemenKaryawan:
    def __init__(self):
        self.daftar_karyawan = []

    def tambah_karyawan(self, Karyawan):
        self.daftar_karyawan.append(Karyawan)

    def tampilkan_semua_karyawan(self):
        print("Daftar Karyawan: ")
        for Karyawan in self.daftar_karyawan:
            Karyawan.info()
            print("-" * 30)

manajer = ManajemenKaryawan()

k1 = KaryawanTetap("dian", 5000000, "IT", 1000000)
k2 = KaryawanTetap("ferdi", 4500000, "SS", 900000)
k3 = KaryawanHarian("wildan", 2500000, "Teknisi", 11)
k4 = KaryawanHarian("putra", 3700000, "Teknisi", 13)

manajer.tambah_karyawan(k1)
manajer.tambah_karyawan(k2)
manajer.tambah_karyawan(k3)
manajer.tambah_karyawan(k4)

manajer.tampilkan_semua_karyawan()