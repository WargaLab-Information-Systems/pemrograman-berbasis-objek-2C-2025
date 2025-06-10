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
    print(f"Gaji {karyawan.nama} : Rp {karyawan.hitung_gaji()}")

while True:
    print("\n=== Pilih jenis karyawan ===")
    print("1. Karyawan Tetap")
    print("2. Karyawan Kontrak")
    pilihan = int(input("Masukkan pilihan (1/2): "))

    nama = input("Masukkan nama karyawan: ")

    if pilihan == 1:
        print("\n--- Karyawan Tetap ---")
        gaji_bulanan = int(input("Masukkan gaji bulanan : "))
        karyawan = KaryawanTetap(nama, gaji_bulanan)
        cetak_gaji(karyawan)
    elif pilihan == 2:
        print("\n--- Karyawan Kontrak ---")
        jam_kerja = int(input("Masukkan total jam kerja/hari : "))
        if 0 < jam_kerja <= 24:
            upah_per_jam = int(input("Masukkan upah per jam    : "))
            karyawan = KaryawanKontrak(nama, jam_kerja, upah_per_jam)
            cetak_gaji(karyawan)
        else:
            print("-- inputan anda invalid harus (1-24) --")

        
    else:
        print("-- Pilihan tidak valid --")

    ulang = input("\nMau ngulang? (y/n): ")
    if ulang != 'y':
        print("\n--- Program selesai ---")
        break

