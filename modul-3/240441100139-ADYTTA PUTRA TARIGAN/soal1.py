class Karyawan:
    def __init__(self, nama, gaji, departemen):
        self.nama = nama
        self.gaji = gaji
        self.departemen = departemen

    def tampilkan_info(self):
        return f"Nama: {self.nama}, Gaji: {self.gaji}, Departemen: {self.departemen}"

class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji, departemen, tunjangan):
        super().__init__(nama, gaji, departemen)
        self.tunjangan = tunjangan

    def tampilkan_info(self):
        return f"{super().tampilkan_info()}, Tunjangan: {self.tunjangan}"

class KaryawanHarian(Karyawan):
    def __init__(self, nama, gaji, departemen, jam_kerja):
        super().__init__(nama, gaji, departemen)
        self.jam_kerja = jam_kerja
    
    def tampilkan_info(self):
        return f"{super().tampilkan_info()}, Jam Kerja: {self.jam_kerja}"

class ManajemenKaryawan:
    def __init__(self):
        self.daftar_karyawan = []
    
    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_semua_karyawan(self):
        for karyawan in self.daftar_karyawan:
            print(karyawan.tampilkan_info())
    
manajemen = ManajemenKaryawan()

karyawan_tetap_1 = KaryawanTetap("Adytta", 5000000, "HR", 1000000)
karyawan_tetap_2 = KaryawanTetap("Fauzi", 6000000, "Finance", 1200000)
karyawan_harian_1 = KaryawanHarian("Teddy", 3000000, "Marketing", 8)
karyawan_harian_2 = KaryawanHarian("Abdul", 3500000, "Sales", 7)

manajemen.tambah_karyawan(karyawan_tetap_1)
manajemen.tambah_karyawan(karyawan_tetap_2)
manajemen.tambah_karyawan(karyawan_harian_1)
manajemen.tambah_karyawan(karyawan_harian_2)

manajemen.tampilkan_semua_karyawan()