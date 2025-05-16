class Karyawan:
    def __init__(self, nama, gaji, departemen):
        self.nama = nama
        self.gaji = gaji
        self.departemen = departemen
    def info(self):
        print(f"- {self.nama} dengan gaji {self.gaji} yang berada di departemen {self.departemen}")

class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji, departemen, tunjangan):
        super().__init__(nama, gaji, departemen)
        self.tunjangan = tunjangan
    def info(self):
        print(f"- {self.nama} Karyawan tetap mempunyai tunjangan {self.tunjangan} dan gaji tetap {self.gaji}")

class KaryawanHarian(Karyawan):
    def __init__(self, nama, gaji_per_jam, departemen, jam_kerja):
        super().__init__(nama, 0, departemen) 
        self.gaji_per_jam = gaji_per_jam
        self.jam_kerja = jam_kerja
    def hitung_gaji(self):
        return self.gaji_per_jam * self.jam_kerja 
    def info(self):
        gaji_harian = self.hitung_gaji() 
        print(f"- {self.nama} dari departemen {self.departemen} bekerja {self.jam_kerja} jam dengan upah {self.gaji_per_jam}/jam. Total gaji: {gaji_harian}")

class ManajemenKaryawan:
    def __init__(self):
        self.daftar_karyawan = []
    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)
    def tampilkan_semua_karyawan(self):
        for karyawan in self.daftar_karyawan:
            karyawan.info()

manajemen = ManajemenKaryawan()
while True:
    print("\n1. Tetap")
    print("2. Harian")
    jenis_karyawan = int(input("silahkan inputkan nomor Karyawan: "))
    nama = input("Nama Karyawan: ")
    departemen = input("Departemen: ")
    if jenis_karyawan == 1:
        gaji = int(input("Gaji Bulanan: "))
        tunjangan = input("Mempunyai tunjangan: ")
        karyawan = KaryawanTetap(nama, gaji, departemen, tunjangan)
        manajemen.tambah_karyawan(karyawan)
    elif jenis_karyawan == 2:
        gaji_per_jam = int(input("gaji per jam: "))
        jamkerja = int(input("Jam kerja: "))
        karyawan = KaryawanHarian(nama, gaji_per_jam, departemen, jamkerja)
        manajemen.tambah_karyawan(karyawan)
    else:
        print("Jenis karyawan yang anda input tidak valid")
        continue
    ulang = input("Apakah anda ingin menginputkan ulang? (y/n) ")
    if ulang.lower() != "y":
        break
    
print("\n---- DAFTAR PEGAWAI ----")
manajemen.tampilkan_semua_karyawan()