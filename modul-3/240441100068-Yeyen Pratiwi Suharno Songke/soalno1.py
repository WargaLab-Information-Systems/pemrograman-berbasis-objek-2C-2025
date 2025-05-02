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
        super().info()
        print(f"Tunjangan: {self.tunjangan}")
        print("-" * 30)

class KaryawanHarian(Karyawan):
    def __init__(self, nama, gaji, departemen, jam_kerja):
        super().__init__(nama, gaji, departemen)
        self.jam_kerja = jam_kerja

    def info(self):
        super().info()
        print(f"Jam Kerja per Hari: {self.jam_kerja} jam")
        print("-" * 30)

class ManajemenKaryawan:
    def __init__(self):
        self.daftar_karyawan = []

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_semua_karyawan(self):
        for karyawan in self.daftar_karyawan:
            karyawan.info()

manajemen = ManajemenKaryawan()

karyawan_tetap1 = KaryawanTetap("Agista", 5000000, "HR", 100000)
karyawan_harian1 = KaryawanHarian("Adi", 3000000, "IT", 8)
karyawan_harian2 = KaryawanHarian("Salsa", 2400000, "Sales & Marketing", 5)
karyawan_tetap2 = KaryawanTetap("Sulton", 1600000, "IT", 80000)

manajemen.tambah_karyawan(karyawan_tetap1)
manajemen.tambah_karyawan(karyawan_harian2)
manajemen.tambah_karyawan(karyawan_tetap2)
manajemen.tambah_karyawan(karyawan_harian1)

manajemen.tampilkan_semua_karyawan()
