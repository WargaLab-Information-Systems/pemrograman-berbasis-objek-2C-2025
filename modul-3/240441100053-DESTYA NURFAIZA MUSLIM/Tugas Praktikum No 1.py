class Karyawan:
    def __init__(self, nama, gaji, departemen):
        self.nama = nama
        self.gaji = gaji
        self.departemen = departemen
    
    def info(self):
        print(f"Nama : {self.nama} \nGaji : {self.gaji} \nDepartemen : {self.departemen}")

class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji, departemen, tunjangan):
        super().__init__(nama, gaji, departemen)
        self.tunjangan = tunjangan
    
    def info(self):
        print()
        print("======Karyawan Tetap======")
        super().info()
        print(f"Jumlah Tunjangan : {self.tunjangan}")

class KaryawanHarian(Karyawan):
    def __init__(self, nama, gaji, departemen, jam_kerja):
        super().__init__(nama, gaji, departemen)
        self.jam_kerja = jam_kerja

    def info(self):
        print()
        print("======Karyawan Harian=======")
        super().info()
        print(f"Jam Kerja per Hari : {self.jam_kerja} Jam")

class ManajemenKaryawan:
    def __init__(self):
        self.daftar_karyawan = []

    def tambah_karyawan(self,karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_semua_karyawan(self):
        for karyawan in self.daftar_karyawan:
            karyawan.info()

manajemen = ManajemenKaryawan()
k1 = KaryawanTetap("Karto", 5000000, "Periklanan", 30000000)
k2 = KaryawanTetap("Suharti", 7000000, "IT", 15000000)
k3 = KaryawanHarian("Sartimi", 2500000, "Penjualan", 6)
k4 = KaryawanHarian("Pardi", 2000000, "Periklanan", 8)

manajemen.tambah_karyawan(k1)
manajemen.tambah_karyawan(k2)
manajemen.tambah_karyawan(k3)
manajemen.tambah_karyawan(k4)

manajemen.tampilkan_semua_karyawan()