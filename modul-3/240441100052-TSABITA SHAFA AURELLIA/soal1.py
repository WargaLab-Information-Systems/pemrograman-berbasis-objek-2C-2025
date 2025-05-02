
class Karyawan:
    def __init__(self, nama, gaji, departemen):
        self.nama = nama
        self.gaji = gaji
        self.departemen = departemen

    def info(self):
        print(f"Nama       : {self.nama}")
        print(f"Gaji       : {self.gaji}")
        print(f"Departemen : {self.departemen}")


class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji, departemen, tunjangan):
        super().__init__(nama, gaji, departemen)
        self.tunjangan = tunjangan

    def info(self):
        super().info()
        print(f"Tunjangan  : {self.tunjangan}")
        print("Status     : Karyawan Tetap\n")


class KaryawanHarian(Karyawan):
    def __init__(self, nama, gaji, departemen, jam_kerja):
        super().__init__(nama, gaji, departemen)
        self.jam_kerja = jam_kerja

    def info(self):
        super().info()
        print(f"Jam Kerja  : {self.jam_kerja} jam/hari")
        print("Status     : Karyawan Harian\n")


class ManajemenKaryawan:
    def __init__(self):
        self.daftar_karyawan = []

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_semua_karyawan(self):
        print("== Daftar Semua Karyawan ==")
        for karyawan in self.daftar_karyawan:
            karyawan.info()


manajemen = ManajemenKaryawan()
manajemen.tambah_karyawan(KaryawanTetap("rafa", 5000000, "IT", 1000000))
manajemen.tambah_karyawan(KaryawanTetap("bita", 4500000, "HRD", 900000))
manajemen.tambah_karyawan(KaryawanHarian("lia", 100000, "Produksi", 8))
manajemen.tambah_karyawan(KaryawanHarian("Tono", 120000, "Logistik", 7))
manajemen.tampilkan_semua_karyawan()
