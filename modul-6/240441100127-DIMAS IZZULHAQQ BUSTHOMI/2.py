from abc import ABC, abstractmethod

class Karyawan(ABC):
    @abstractmethod
    def hitung_gaji(self):
        pass

class KaryawanTetap(Karyawan):
    def __init__(self, hari, gaji):
        self.hari = hari
        self.gaji = gaji
    
    def hitung_gaji(self):
        return self.gaji * self.hari 
    
class KaryawanKontrak(Karyawan):
    def __init__(self, jam_kerja, gaji):
        self.jam_kerja = jam_kerja
        self.gaji = gaji

    def hitung_gaji(self):
        return self.gaji * self.jam_kerja
    
def show_salary(karyawan):
    return karyawan.hitung_gaji()

while True:
    print("===== PILIH KARYAWAN =====")
    print("1. Karyawan Tetap")
    print("2. Karyawan Kontrak")

    choice = input("Pilih menu : ")
    if choice == "1":
        while True:
            print("===== MASUKKAN DATA KARYAWAN TETAP =====")
            hari = input("Masukkan berapa hari bekerja (perminggu) : ")
            gaji = input("Masukkan Gaji : ")
            if hari.isdigit() and gaji.isdigit():
                hari = int(hari)
                gaji = int(gaji)
                kt = KaryawanTetap(hari, gaji)
                print(f"Gaji karyawan tetap   : {show_salary(kt)}")
                break
            else:
                print("Input harus Angka!-")

    elif choice == "2":
        while True:
            print("===== MASUKKAN DAFTAR KARYAWAN KONTRAK =====")
            jam = input("Masukkan Jam Kerja Harian : ")
            gaji = input("Masukkan Gaji Perjam Kerja : ")
            if jam.isdigit() and gaji.isdigit():
                jam = int(jam)
                gaji = int(gaji)
                kk = KaryawanKontrak(jam, gaji)
                print(f"Gaji karyawan kontrak : {show_salary(kk)}")
                break
            else:
                print("Input harus Angka!-")


