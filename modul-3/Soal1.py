class karyawan:
    def __init__(self, nama, gaji, departemen):
        self.nama = nama
        self.gaji = gaji
        self.departemen = departemen

    def info(self):
        print(f"Nama       : {self.nama}")
        print(f"Gaji       : {self.gaji}")
        print(f"Departemen : {self.departemen}")

class karyawantetap(karyawan):
    def __init__(self, nama, gaji, departemen, tunjangan):
        super().__init__(nama, gaji, departemen)
        self.tunjangan = tunjangan

    def info(self):
        print("=== Karyawan Tetap ===")
        super().info()
        print(f"Tunjangano  : {self.tunjangan}") 
        print("-" * 30)

class karyawanharian(karyawan):
    def __init__(self, nama, gaji, departemen, jam_kerja):
        super().__init__(nama, gaji, departemen)
        self.jam_kerja = jam_kerja

    def info(self):
        print("=== Karyawan Harian ===")
        super().info()
        print(f"Jam Kerja  : {self.jam_kerja} Jam/Hari")
        print("-" * 30)

class manajemenkaryawan:
    def __init__(self):
        self.daftar_karyawan = []

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_semua_karyawan(self):
        for karyawan in self.daftar_karyawan:
            karyawan.info()

manajemen = manajemenkaryawan()

karyawan1 = karyawantetap("Sulis", 3000000, "Keuangan", 100000)
karyawan2 = karyawanharian("Sugianto", 2000000, "Produksi", 6) 

manajemen.tambah_karyawan(karyawan1)
manajemen.tambah_karyawan(karyawan2)
manajemen.tampilkan_semua_karyawan()