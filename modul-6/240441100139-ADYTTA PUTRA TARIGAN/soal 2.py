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
    def __init__(self, nama, jam_kerja, upah_per_jam):
        super().__init__(nama)
        self.jam_kerja = jam_kerja
        self.upah_per_jam = upah_per_jam

    def hitung_gaji(self):
        return self.jam_kerja * self.upah_per_jam

def cetak_gaji(karyawan):
    print(f"Gaji {karyawan.nama}: Rp {karyawan.hitung_gaji()}")

while True:
    print("\nPilih jenis karyawan:")
    print("1. Karyawan Tetap")
    print("2. Karyawan Kontrak")
    print("3. Keluar")

    pilihan = int(input("Masukkan pilihan (1/2/3): "))

    if pilihan == 1 :
        nama = input("Nama karyawan: ")
        gaji = float(input("Gaji bulanan: Rp "))
        karyawan = KaryawanTetap(nama, gaji)
        cetak_gaji(karyawan)

    elif pilihan == 2 :
        nama = input("Nama karyawan: ")
        jam = float(input("Jumlah jam kerja: "))
        upah = float(input("Upah per jam: Rp "))
        karyawan = KaryawanKontrak(nama, jam, upah)
        cetak_gaji(karyawan)

    elif pilihan == 3 :
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid. Coba lagi.")
