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
        print("[Karyawan Tetap]")
        print(f"Nama       : {self.nama}")
        print(f"Gaji       : {self.gaji}")
        print(f"Tunjangan  : {self.tunjangan}")
        print(f"Departemen : {self.departemen}")

class KaryawanHarian(Karyawan):
    def __init__(self, nama, gaji, departemen, jam_kerja):
        super().__init__(nama, gaji, departemen)
        self.jam_kerja = jam_kerja

    def info(self):
        print("[Karyawan Harian]")
        print(f"Nama       : {self.nama}")
        print(f"Gaji       : {self.gaji}")
        print(f"Jam Kerja  : {self.jam_kerja} jam/hari")
        print(f"Departemen : {self.departemen}")

class ManajemenKaryawan:
    def __init__(self):
        self.daftar_karyawan = []

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_semua_karyawan(self):
        print("\n=== Daftar Semua Karyawan ===")
        for karyawan in self.daftar_karyawan:
            karyawan.info()
            print("-" * 30)

def input_angka(prompt):
    while True:
        nilai = input(prompt)
        if nilai.isdigit():
            return int(nilai)
        else:
            print("Input harus berupa angka. Silakan ulangi.")

manajemen = ManajemenKaryawan()
while True:
    print("\nMasukkan data karyawan")
    jenis = input("Jenis karyawan (tetap/harian, ketik 'selesai' untuk keluar): ").lower()

    if jenis == 'selesai':
        break
    elif jenis not in ['tetap', 'harian']:
        print("Jenis karyawan tidak dikenali. Ulangi input.")
        continue

    nama = input("Nama: ")
    gaji = input_angka("Gaji: ")
    departemen = input("Departemen: ")

    if jenis == 'tetap':
        tunjangan = input_angka("Tunjangan: ")
        karyawan = KaryawanTetap(nama, gaji, departemen, tunjangan)
    elif jenis == 'harian':
        jam_kerja = input_angka("Jam kerja per hari: ")
        karyawan = KaryawanHarian(nama, gaji, departemen, jam_kerja)

    manajemen.tambah_karyawan(karyawan)
    print("Karyawan berhasil ditambahkan!")

manajemen.tampilkan_semua_karyawan()