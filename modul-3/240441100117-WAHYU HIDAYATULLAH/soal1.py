class Karyawan:
    def __init__(self, nama, gaji, departemen):
        self.nama = nama
        self.gaji = gaji
        self.departemen = departemen

    def info(self):
        print(f"Nama       : {self.nama}")
        print(f"Gaji       : Rp{self.gaji}")
        print(f"Departemen : {self.departemen}")

class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji, departemen, tunjangan):
        super().__init__(nama, gaji, departemen)
        self.tunjangan = tunjangan

    def info(self):
        super().info()
        print(f"Tunjangan  : Rp{self.tunjangan}")
        print("Status     : Karyawan Tetap")

class KaryawanHarian(Karyawan):
    def __init__(self, nama, gaji, departemen, jam_kerja):
        super().__init__(nama, gaji, departemen)
        self.jam_kerja = jam_kerja

    def info(self):
        super().info()
        print(f"Jam Kerja Per Hari : {self.jam_kerja} jam")
        print("Status     : Karyawan Harian")
        print("=" * 30)

class ManajemenKaryawan:
    def __init__(self):
        self.daftar_karyawan = []

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_semua_karyawan(self):
        print("\n=== Daftar Seluruh Karyawan ===")
        for karyawan in self.daftar_karyawan:
            karyawan.info()

manajemen = ManajemenKaryawan()

while True:
    print("\nTambah Karyawan Baru")
    jenis = input("Jenis Karyawan (tetap/harian): ")
    if jenis == "tetap":
        nama = input("Masukkan Nama Karyawan : ")
        gaji = int(input("Masukkan Gaji : Rp"))
        departemen = input("Departemen : ")
        tunjangan = int(input("Tunjangan : Rp"))
        karyawan = KaryawanTetap(nama, gaji, departemen, tunjangan)
    elif jenis == "harian":
        nama = input("Masukkan Nama Karyawan : ")
        gaji = int(input("Masukkan Gaji : Rp"))
        departemen = input("Departemen : ")
        jam_kerja = int(input("Jam kerja per hari (jam): "))
        karyawan = KaryawanHarian(nama, gaji, departemen, jam_kerja)
    else:
        print("Jenis Karyawan tidak dikenal")
        continue

    manajemen.tambah_karyawan(karyawan)

    n = input("Tambah karyawan lagi? (y/n): ")
    if n.lower() != 'y':
        break

manajemen.tampilkan_semua_karyawan()