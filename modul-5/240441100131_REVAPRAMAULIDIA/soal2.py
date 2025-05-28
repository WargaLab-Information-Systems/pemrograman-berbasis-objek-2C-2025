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
def input_angka(pesan):
    while True:
        nilai = input(pesan)
        if nilai.isdigit():
            return int(nilai)
        else:
            print("Masukkan hanya angka")

def cetak_gaji(karyawan):
    print("Gaji", karyawan.nama, karyawan.hitung_gaji())

print("Pilih jenis karyawan")
print("1.Karywan Tetap")
print("2. Karywan Kontrak")

pilihan=input("Masukkan pilihan (1/2):")
nama=input("Masukkan nama karywan:")

if pilihan == "1":
    gaji = input_angka("Masukkan gaji bulanan: ")
    bonus=input_angka("Masukkan bonus:")
    karyawan = KaryawanTetap(nama, gaji,bonus)
    cetak_gaji(karyawan)

elif pilihan == "2":
    jam = input_angka("Masukkan jumlah jam kerja: ")
    upah = input_angka("Masukkan upah per jam: ")
    karyawan = KaryawanKontrak(nama, jam, upah)
    cetak_gaji(karyawan)

else:
    print("Pilihan tidak valid")