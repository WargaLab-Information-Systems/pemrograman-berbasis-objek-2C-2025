class Karyawan:
    def __init__(self, nama, gaji, departemen):
        self.nama = nama
        self.gaji = gaji
        self.departemen = departemen
    def info(self):
        print(f"Nama               : {self.nama}")
        print(f"Gaji               : Rp. {self.gaji}")
        print(f"Departemen         : {self.departemen}")

class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji, departemen, tunjangan):
        super().__init__(nama, gaji, departemen)
        self.tunjangan = tunjangan
    def info(self):
        print("---Karyawan Tetap---")
        super().info()
        print(f"Tunjangan per bulan: Rp.{self.tunjangan}")
        print("\n")

class KaryawanHarian(Karyawan):
    def __init__(self, nama, gaji, departemen, jam_kerja):
        super().__init__(nama, gaji, departemen)
        self.jam_kerja = jam_kerja
    def info(self):
        print("---Karyawan Harian---")
        super().info()
        print(f"Jam kerja per hari : {self.jam_kerja} jam")
        print("\n")

class ManajemenKaryawan:
    daftar_karyawan = []
    @classmethod
    def tambah_karyawan_tetap(cls, nama, gaji, departemen, tunjangan):
        karyawan = KaryawanTetap(nama, gaji, departemen, tunjangan)
        cls.daftar_karyawan.append(karyawan)
    @classmethod
    def tambah_karyawan_harian(cls, nama, gaji, departemen, jam_kerja):
        karyawan = KaryawanHarian(nama, gaji, departemen, jam_kerja)
        cls.daftar_karyawan.append(karyawan)
    @classmethod
    def tampilkan_semua_karyawan (cls):
        for k in cls.daftar_karyawan:
            k.info()

karyawan1 = ManajemenKaryawan.tambah_karyawan_tetap("Amin", 4500000, "Keuangan", 200000)
karyawan2 = ManajemenKaryawan.tambah_karyawan_tetap("Bolang", 4000000, "IT", 300000)
karyawan3 = ManajemenKaryawan.tambah_karyawan_harian("Unyil", 3000000, "Pemasaran", 8)
karyawan4 = ManajemenKaryawan.tambah_karyawan_harian("Gurt", 3500000, "SDM", 7.5)
ManajemenKaryawan.tampilkan_semua_karyawan()