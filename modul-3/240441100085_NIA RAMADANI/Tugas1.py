class Karyawan:
    def __init__(self, nama, gaji, departemen):
        self.nama = nama
        self.gaji = gaji
        self.departemen = departemen

    def info(self):
        print("Nama:", self.nama)
        print("Gaji:", self.gaji)
        print("Departemen:", self.departemen)


class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji, departemen, tunjangan):
        super().__init__(nama, gaji, departemen)
        self.tunjangan = tunjangan

    def info(self):
        print("Karyawan Tetap:")
        super().info()
        print("Tunjangan:", self.tunjangan)
        print()


class KaryawanHarian(Karyawan):
    def __init__(self, nama, gaji, departemen, jam_kerja):
        super().__init__(nama, gaji, departemen)
        self.jam_kerja = jam_kerja

    def info(self):
        print("Karyawan Harian:")
        super().info()
        print("Jam Kerja:", self.jam_kerja)
        print()


class ManajemenKaryawan:
    def __init__(self):
        self.daftar_karyawan = []

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_semua_karyawan(self):
        for karyawan in self.daftar_karyawan:
            karyawan.info()


manajemen = ManajemenKaryawan()

manajemen.tambah_karyawan(KaryawanTetap("Ali", 5000000, "IT", 1000000))
manajemen.tambah_karyawan(KaryawanTetap("Siti", 6000000, "HRD", 1200000))
manajemen.tambah_karyawan(KaryawanHarian("Budi", 150000, "Produksi", 8))
manajemen.tambah_karyawan(KaryawanHarian("Dina", 130000, "Gudang", 7))

manajemen.tampilkan_semua_karyawan()
