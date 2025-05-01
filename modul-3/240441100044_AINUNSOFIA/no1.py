# membuat class induk
class Karyawan:
    def __init__(self, nama, gaji, departemen): #constructor
        self.nama = nama #atribut
        self.gaji = gaji
        self.departemen = departemen

    def info(self): #methode
        print(f"Nama: {self.nama} \nGaji: {self.gaji} \nDepartemen: {self.departemen}")

# Kelas Anak (Karyawan Tetap)
class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji, departemen, tunjangan):
        super().__init__(nama, gaji, departemen)
        self.tunjangan = tunjangan

    def info(self):
        super().info()
        print(f"Tunjangan: {self.tunjangan}")
        print("Status: Karyawan Tetap\n")

# Kelas Anak (Karyawan Harian)
class KaryawanHarian(Karyawan):
    def __init__(self, nama, gaji, departemen, jam_kerja):
        super().__init__(nama, gaji, departemen)
        self.jam_kerja = jam_kerja

    def info(self):
        super().info()
        print(f"Jam Kerja per Hari: {self.jam_kerja}")
        print("Status: Karyawan Harian\n")

# Kelas Manajemen Karyawan
class ManajemenKaryawan:
    def __init__(self):
        self.daftar_karyawan = []

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_semua_karyawan(self):
        print("Daftar Semua Karyawan:")
        for karyawan in self.daftar_karyawan:
            karyawan.info()

# Membuat objek 
manajemen = ManajemenKaryawan()

karyawan1 = KaryawanTetap("Ainun", 7000000, "IT", 2000000)
karyawan2 = KaryawanHarian("Naisa", 100000, "Produksi", 8)
karyawan3 = KaryawanTetap("Hilmy", 8000000, "HRD", 2500000)
karyawan4 = KaryawanHarian("Jefri", 120000, "Marketing", 7)

# Menambahkan ke manajemen
manajemen.tambah_karyawan(karyawan1)
manajemen.tambah_karyawan(karyawan2)
manajemen.tambah_karyawan(karyawan2)
manajemen.tambah_karyawan(karyawan4)

# Menampilkan semua karyawan
manajemen.tampilkan_semua_karyawan()