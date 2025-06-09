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

# Polymorphism
def cetak_gaji(karyawan):
    print(f"Gaji {karyawan.nama} ({karyawan.__class__.__name__}): Rp{karyawan.hitung_gaji():,.2f}")

daftar_karyawan = []

while True:
    print("\nTambah Karyawan:")
    print("1. Karyawan Tetap𓂃𓏧♡")
    print("2. Karyawan Kontrak𓂃𓏧♡")
    print("3. Selesai𓂃𓏧♡")
    pilihan = input("Masukkan pilihan (1,2,3): ")

    if pilihan == "1":
        nama = input("Nama karyawan tetap: ")
        gaji = float(input("Gaji bulanan: "))
        daftar_karyawan.append(KaryawanTetap(nama, gaji))
    elif pilihan == "2":
        nama = input("Nama karyawan kontrak: ")
        jam = float(input("Jumlah jam kerja: "))
        upah = float(input("Upah per jam: "))
        daftar_karyawan.append(KaryawanKontrak(nama, jam, upah))
    elif pilihan == "3":
        break
    else:
        print("Pilihan tidak valid. Coba lagiᵔ ᵕ ᵔ")

print("\n❀ Ini daftar gaji karyawan ❀")
for karyawan in daftar_karyawan:
    cetak_gaji(karyawan)
