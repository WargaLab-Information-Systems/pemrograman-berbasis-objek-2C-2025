class Karyawan:
    def __init__(self, nama, gaji, departemen):
        self.nama = nama
        self.gaji = gaji
        self.departemen = departemen

    def info(self):
        print(f"Nama: {self.nama}, Gaji: {self.gaji}, Departemen: {self.departemen}")

class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji, departemen, tunjangan):
        super().__init__(nama, gaji, departemen)
        self.tunjangan = tunjangan

    def info(self):
        print(f"Nama: {self.nama}, Gaji: {self.gaji}, Departemen: {self.departemen}, Tunjangan: {self.tunjangan}")

class KaryawanHarian(Karyawan):
    def __init__(self, nama, gaji, departemen, jam_kerja):
        super().__init__(nama, gaji, departemen)
        self.jam_kerja = jam_kerja

    def info(self):
        print(f"Nama: {self.nama}, Gaji: {self.gaji}, Departemen: {self.departemen}, Jam Kerja: {self.jam_kerja} jam/hari")

class ManajemenKaryawan:
    def __init__(self):
        self.daftar_karyawan = []

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_semua_karyawan(self):
        for karyawan in self.daftar_karyawan:
            karyawan.info()

manajemen = ManajemenKaryawan()

karyawan1 = KaryawanTetap("Budi", 5000000, "IT", 100000)
karyawan2 = KaryawanTetap("Siti", 4500000, "HR", 75000)

karyawan3 = KaryawanHarian("Joko", 1500000, "Marketing", 8)
karyawan4 = KaryawanHarian("Dewi", 1200000, "Sales", 6)

manajemen.tambah_karyawan(karyawan1)
manajemen.tambah_karyawan(karyawan2)
manajemen.tambah_karyawan(karyawan3)
manajemen.tambah_karyawan(karyawan4)

manajemen.tampilkan_semua_karyawan()
