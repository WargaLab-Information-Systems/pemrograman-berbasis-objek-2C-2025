from abc import ABC, abstractmethod

class Karyawan(ABC):
    @abstractmethod
    def hitung_gaji(self):
        pass

class KaryawanTetap(Karyawan):
    def __init__(self, gaji_pokok):
        self.gaji_pokok = gaji_pokok

    def hitung_gaji(self):
        return self.gaji_pokok + (0.1 * self.gaji_pokok) 

class KaryawanKontrak(Karyawan):
    def __init__(self, jam_kerja, upah_per_jam):
        self.jam_kerja = jam_kerja
        self.upah_per_jam = upah_per_jam

    def hitung_gaji(self):
        return self.jam_kerja * self.upah_per_jam

def cetak_gaji(karyawan):
    print("Gaji Karyawan: Rp", karyawan.hitung_gaji())

while True:
    print("\n=== Hitung Gaji Karyawan ===")
    print("1. Karyawan Tetap")
    print("2. Karyawan Kontrak")
    print("3. Keluar")
    pilihan = input("Pilih jenis karyawan: ")

    if pilihan == '1':
        gaji_pokok = float(input("Masukkan gaji pokok: Rp "))
        karyawan = KaryawanTetap(gaji_pokok)
    elif pilihan == '2':
        jam_kerja = float(input("Masukkan jumlah jam kerja: "))
        upah_per_jam = float(input("Masukkan upah per jam: Rp "))
        karyawan = KaryawanKontrak(jam_kerja, upah_per_jam)
    elif pilihan == '3':
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Coba lagi.")
        continue

    cetak_gaji(karyawan)
