from abc import ABC, abstractmethod

class Karyawan(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def hitung_gaji(self):
        pass

class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji_bulanan):
        super().__init__(nama)
        self.gaji_bulanan = gaji_bulanan

    def hitung_gaji(self):
        return self.gaji_bulanan

class KaryawanKontrak(Karyawan):
    def __init__(self, nama, gaji_per_jam, jumlah_jam):
        super().__init__(nama)
        self.gaji_per_jam = gaji_per_jam
        self.jumlah_jam = jumlah_jam

    def hitung_gaji(self):
        return self.gaji_per_jam * self.jumlah_jam

def cetak_gaji(karyawan):
    print(f"Nama: {karyawan.nama}, Gaji: Rp{int(karyawan.hitung_gaji()):,}")

while True:
    print("\n=== Hitung Gaji Karyawan ===")
    print("1. Karyawan Tetap\n2. Karyawan Kontrak")
    jenis = input("Pilih jenis karyawan (1/2): ")

    nama = input("Masukkan nama karyawan: ")

    if jenis == "1":
        gaji = float(input("Masukkan gaji bulanan: "))
        karyawan = KaryawanTetap(nama, gaji)
    elif jenis == "2":
        gaji_jam = float(input("Masukkan gaji per jam: "))
        jam = int(input("Masukkan jumlah jam kerja: "))
        karyawan = KaryawanKontrak(nama, gaji_jam, jam)
    else:
        print("Pilihan tidak valid!")
        continue

    cetak_gaji(karyawan)

    ulang = input("Ingin menghitung gaji karyawan lain? (y/n): ")
    if ulang != "y":
        break
