class Karyawan:
    def __init__(self, nama, gaji, departemen):
        self.nama = nama # nama tidak diinisialisasi
        self.gaji = gaji
        self.departemen = departemen

    def info(self):
        print(f"Nama: {self.nama}")
        print(f"Gaji: {self.gaji}")
        print(f"Departemen: {self.departemen}")

class KaryawanTetap(Karyawan): # parent classnya dihapus
    def __init__(self, nama, gaji, departemen, tunjangan):
        super().__init__(nama, gaji, departemen)
        self.tunjangan = tunjangan

    def info(self):
        print("∎ Karyawan Tetap ∎")
        super().info()
        print(f"Tunjangan: {self.tunjangan}")
        print("-------------------")

class KaryawanHarian(Karyawan):
    def __init__(self, nama, gaji, departemen, jam_kerja):
        super().__init__(nama, gaji, departemen)
        self.jam_kerja = jam_kerja 

    def info(self):
        print("∎ Karyawan Harian ∎")
        super().info()
        print(f"Jam Kerja: {self.jam_kerja} jam/hari")
        print("-------------------")

class ManajemenKaryawan:
    def __init__(self):
        self.daftar_karyawan = [] # ini tadi diganti ' '

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_semua_karyawan(self):
        for karyawan in self.daftar_karyawan:
            karyawan.info()

kt1 = KaryawanTetap("Zayne", 5000000, "IT", 1000000)
kt2 = KaryawanTetap("Rafayel", 6000000, "Marketing", 2000000)
kh1 = KaryawanHarian("Scara", 3000000, "IT", 8)
kh2 = KaryawanHarian("Caleb", 4000000, "HR", 10)

mk = ManajemenKaryawan()
mk.tambah_karyawan(kt1)
mk.tambah_karyawan(kt2)
mk.tambah_karyawan(kh1)
mk.tambah_karyawan(kh2)

mk.tampilkan_semua_karyawan()   