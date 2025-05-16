class Karyawan:
    def __init__(self,nama, gaji, departemen):
        self.nama = nama
        self.gaji = gaji
        self.departemen = departemen

    def info(self):
        print(f"Nama        : {self.nama}")
        print(f"Gaji        : {self.gaji}")
        print(f"Departemen  : {self.departemen}")
    
class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji, departemen, tunjangan):
        super().__init__(nama, gaji, departemen)
        self.tunjangan = tunjangan
    
    def info(self):
        print("=== Karyawan Tetap ===")
        super().info()
        print(f"Tunjangan : {self.tunjangan}")
        print("------------------------")

class KaryawanHarian(Karyawan):
    def __init__(self, nama, gaji, departemen, jam_kerja):
        super().__init__(nama, gaji, departemen)
        self.jam_kerja = jam_kerja

    def info(self):
        print("===Karyawan Harian ===")
        super().info()
        print(f"Jam kerja : {self.jam_kerja} jam/hari")
        print("------------------------")

class ManajemenKaryawan:
    def __init__(self):
        self.daftar_karyawan = []

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)
    
    def tampilkan_semua_karyawan(self):
        print("=== Daftar Semua Karyawan ===")
        for karyawan in self.daftar_karyawan:
            karyawan.info()

manajemen = ManajemenKaryawan()

karyawan1 = KaryawanTetap("Wulan", 6000000, "IT", 1000000)
karyawan2 = KaryawanTetap("Tanjiro", 7500000, "Pemasaran", 800000)
karyawan3 = KaryawanHarian("Nezuko", 180000, "Penjualan", 8)
karyawan4 = KaryawanHarian("Inoskin", 150000, "Produksi", 7)

manajemen.tambah_karyawan(karyawan1)
manajemen.tambah_karyawan(karyawan2)
manajemen.tambah_karyawan(karyawan3)
manajemen.tambah_karyawan(karyawan4)

manajemen.tampilkan_semua_karyawan()
