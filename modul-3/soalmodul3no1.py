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
        \
        print(f"Tunjangan: {self.tunjangan}")

class KaryawanHarian(Karyawan):
    def __init__(self, nama, gaji, departemen, jam_kerja):
        super().__init__(nama, gaji, departemen)
        self.jam_kerja = jam_kerja
    
    def info(self):
        super().info()
        print(f"Jam Kerja: {self.jam_kerja} jam per hari")

class ManajemenKaryawan:
    def __init__(self):
        self.daftar_karyawan = []
    
    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)
    
    def tampilkan_semua_karyawan(self):
        for karyawan in self.daftar_karyawan:
            karyawan.info()
            print("-" * 30)


manajemen = ManajemenKaryawan()

karyawan1 = KaryawanTetap("Fina", 7000000, "IT", 1000000)
karyawan2 = KaryawanHarian("Luna", 2000000, "Marketing", 7)
karyawan3 = KaryawanTetap("kiki", 6000000, "HR", 1500000)

manajemen.tambah_karyawan(karyawan1)
manajemen.tambah_karyawan(karyawan2)
manajemen.tambah_karyawan(karyawan3)

manajemen.tampilkan_semua_karyawan()
