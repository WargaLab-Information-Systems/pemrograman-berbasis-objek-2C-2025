from abc import ABC, abstractmethod

class Karyawan(ABC):
    @abstractmethod
    def hitung_gaji(self):
        pass

class KaryawanTetap(Karyawan):
    def __init__(self,nama,gaji_bulanan,bonus=0):
        self.nama=nama
        self.gaji_bulanan=gaji_bulanan
        self.bonus=bonus
    def hitung_gaji(self):
        return self.gaji_bulanan + self.bonus
class KaryawanKontrak(Karyawan):
    def __init__(self,nama,jam_kerja,upah_per_jam):
        self.nama=nama
        self.jam_kerja=jam_kerja
        self.upah_per_jam= upah_per_jam
    def hitung_gaji(self):
        return self.jam_kerja * self.upah_per_jam
def input_angka(angka):
    while True:
        nilai = input(angka)
        if nilai.replace('.', '', 1).isdigit():
            return float(nilai)
        else:
            print("Masukkan angka yang valid")

def cetak_gaji(karyawan):
    print("Gaji", karyawan.nama, karyawan.hitung_gaji())
while True:
    print("\n Pilih jenis karyawan")
    print("1.Karywan Tetap")
    print("2. Karywan Kontrak")

    pilihan=int(input("Masukkan pilihan (1/2):"))

    if pilihan == 1:
        nama=input("Masukkan nama karywan:")
        gaji = input_angka("Masukkan gaji bulanan: ")
        bonus=input_angka("Masukkan bonus:")
        karyawan = KaryawanTetap(nama, gaji,bonus)
        cetak_gaji(karyawan)

    elif pilihan == 2:
        nama=input("Masukkan nama karywan:")
        jam = input_angka("Masukkan jumlah jam kerja: ")
        upah = input_angka("Masukkan upah per jam: ")
        karyawan = KaryawanKontrak(nama, jam, upah)
        cetak_gaji(karyawan)
        break
    
    else:
        print("Pilihan tidak valid")