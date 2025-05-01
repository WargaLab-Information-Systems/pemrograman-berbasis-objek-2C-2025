class karyawan :
    def __init__(self, nama, gaji, departemen):
        self.nama = nama
        self.gaji = gaji
        self.departemen = departemen

    def info(self):
        print(f"nama:{self.nama}, gaji{self.gaji}, departemen{self.departemen}")

class karyawantetap(karyawan):
    def __init__(self, nama, gaji, departemen, tunjangan):
        super().__init__(nama, gaji, departemen)
        self.tunjangan = tunjangan

    def info(self):
        print(f"karyawan tetap-nama:{self.nama}, gaji {self.gaji}, departemen {self.departemen}, tunjangan {self.tunjangan}")

class karyawanharian(karyawan):
    def __init__(self, nama, gaji, departemen, jam_kerja):
        super().__init__(nama, gaji, departemen)
        self.jam_kerja = jam_kerja

    def info(self):
        print(f"karyawa harian-nama {self.nama}, gaji {self.gaji}, departemen {self.departemen}, jam kerja {self.jam_kerja} jam/hari")

class manajemenkaryawan:
    def __init__(self):
        self.daftar_karyawan =[]

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_semua_karyawan(self):
        for karyawan in self.daftar_karyawan:
            karyawan.info()

manajemen = manajemenkaryawan()

karyawan1 = karyawantetap("agus", 7000000, "IT", 1500000)
karyawan2 = karyawanharian("anas", 3000000, "produksi", 8)
karyawan3 = karyawantetap("vivi", 8000000, "HRD", 2000000)
karyawan4 = karyawanharian("dina", 2800000, "marketing", 7)

manajemen.tambah_karyawan(karyawan1)
manajemen.tambah_karyawan(karyawan2)
manajemen.tambah_karyawan(karyawan3)
manajemen.tambah_karyawan(karyawan4)

manajemen.tampilkan_semua_karyawan()