class Karyawan:
    def __init__(self, nama, gaji, departemen):
        self.nama = nama
        self.gaji = gaji
        self.departemen = departemen

    def info(self):
        print(f"Nama: {self.nama}")
        print(f"Gaji: {self.gaji}")
        print(f"Departemen: {self.departemen}")

class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji, departemen, tunjangan):
        super().__init__(nama, gaji, departemen)
        self.tunjangan = tunjangan

    def info(self):
        super().info()
        print(f"Tunjangan: {self.tunjangan}")

class KaryawanHarian(Karyawan):
    def __init__(self, nama, gaji, departemen, jam_kerja):
        super().__init__(nama, gaji, departemen)
        self.jam_kerja = jam_kerja

    def info(self):
        super().info()
        print(f"Jam kerja per hari: {self.jam_kerja}")

class ManajemenKaryawan:
    def __init__(self):
        self.daftar_karyawan = []

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_semua_karyawan(self):
        if not self.daftar_karyawan:
            print("Tidak ada karyawan untuk ditampilkan.")
        for karyawan in self.daftar_karyawan:
            karyawan.info()

manajemen = ManajemenKaryawan()

while True:
    print("\nTambah karyawan baru:")
    while True:
        jenis_karyawan = input("Masukkan jenis karyawan (tetap/harian): ")
        if jenis_karyawan == "tetap" or jenis_karyawan == "harian":
            break
        else:
            print("Jenis karyawan tidak valid! Silakan pilih 'tetap' atau 'harian'.")
    nama = input("Nama Karyawan: ")

    while True:
        gaji = input("Gaji: ")
        if gaji.isdigit():  
            gaji = int(gaji)  
            break
        else:
            print("Input gaji harus berupa angka, silakan coba lagi.")

    departemen = input("Departemen: ")

    if jenis_karyawan == "tetap":
        while True:
            tunjangan = input("Tunjangan: ")
            if tunjangan.isdigit(): 
                tunjangan = int(tunjangan) 
                break
            else:
                print("Input tunjangan harus berupa angka, silakan coba lagi.")
        karyawan = KaryawanTetap(nama, gaji, departemen, tunjangan)

    elif jenis_karyawan == "harian":
        while True:
            jam_kerja = input("Jam kerja per hari: ")
            if jam_kerja.isdigit(): 
                jam_kerja = int(jam_kerja)  
                break
            else:
                print("Input jam kerja harus berupa angka, silakan coba lagi.")
        karyawan = KaryawanHarian(nama, gaji, departemen, jam_kerja)

    manajemen.tambah_karyawan(karyawan)

    while True:
        lanjut = input("\nTambah karyawan lagi? (iya/tidak): ")
        if lanjut == "iya" or lanjut == "tidak":
            break
        else:
            print("Input tidak sesuai Harap masukkan 'iya' atau 'tidak'.")

    if lanjut != "iya":
        break

print("\nDaftar semua karyawan:")
manajemen.tampilkan_semua_karyawan()