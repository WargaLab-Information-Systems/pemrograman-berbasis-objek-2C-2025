from abc import ABC, abstractmethod

class Karyawan(ABC):
    @abstractmethod
    def hitung_gaji(self):
        pass

class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji_pokok):
        self.nama = nama
        self.gaji_pokok = gaji_pokok

    def hitung_gaji(self):
        return self.gaji_pokok

class KaryawanKontrak(Karyawan):
    def __init__(self, nama, jam_kerja, upah_per_jam):
        self.nama = nama
        self.jam_kerja = jam_kerja
        self.upah_per_jam = upah_per_jam

    def hitung_gaji(self):
        return self.jam_kerja * self.upah_per_jam

def cetak_gaji(karyawan):
    print(f"Gaji {karyawan.nama}: {karyawan.hitung_gaji()}")

def main():
    print("Program Penghitungan Gaji Karyawan")
    jenis = input("Masukkan jenis karyawan (tetap/kontrak): ").strip().lower()
    nama = input("Masukkan nama karyawan: ")

    if jenis == "tetap":
        gaji_pokok = int(input("Masukkan gaji pokok: "))
        karyawan = KaryawanTetap(nama, gaji_pokok)
    elif jenis == "kontrak":
        jam_kerja = int(input("Masukkan jumlah jam kerja: "))
        upah_per_jam = int(input("Masukkan upah per jam: "))
        karyawan = KaryawanKontrak(nama, jam_kerja, upah_per_jam)
    else:
        print("Jenis karyawan tidak valid.")
        exit()

    cetak_gaji(karyawan)

main()