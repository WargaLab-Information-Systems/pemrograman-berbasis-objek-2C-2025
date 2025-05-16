class Karyawan:
    def __init__(self,nama,gaji,departemen):
        self.nama= nama
        self.gaji= gaji
        self.departemen = departemen
        
    def tampilkan_info(self):
        print(f"nama: {self.nama}")
        print(f"gaji: {self.gaji}")
        print(f"departemen: {self.departemen}")
        
class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji, departemen, tunjangan):
        super().__init__(nama, gaji, departemen)
        self.tunjangan = tunjangan
        
    def tampilkan_info(self):
        print("--karyawan tetap--")
        super().tampilkan_info()
        print(f"tunjangan: {self.tunjangan}")
        print()
        
class KaryawanHarian(Karyawan):
    def __init__(self, nama, gaji, departemen, jam_kerja):
        super().__init__(nama, gaji, departemen)
        self.jam_kerja = jam_kerja
        
    def tampilkan_info(self):
        print("--karyawan harian--")
        super().tampilkan_info()
        print(f"jam kerja per-hari: {self.jam_kerja} jam")
        print()
        
class ManajemenKaryawan:
    def __init__(self):
        self.karyawan_list= []
        
    def tambah_karyawan(self,Karyawan):
        self.karyawan_list.append(Karyawan)
        
    def tampilkan_semua_karyawan(self):
        print("==daftar karyawan==")
        for karyawan in self.karyawan_list:
            karyawan.tampilkan_info()
            
            
manajemen = ManajemenKaryawan()

Karyawan1 = KaryawanTetap("Sri", 40000000, "keuangan", 11000000)
karyawan2 = KaryawanTetap("Agung purba", 67000000, "HRD", 20000000)
karyawan3 = KaryawanHarian("Tamara", 10000000,"packing", 7)
karyawan4 = KaryawanHarian("Gita", 1800000, "produksi divisi VA", 8)

manajemen.tambah_karyawan(Karyawan1)
manajemen.tambah_karyawan(karyawan2)
manajemen.tambah_karyawan(karyawan3)
manajemen.tambah_karyawan(karyawan4)

manajemen.tampilkan_semua_karyawan()