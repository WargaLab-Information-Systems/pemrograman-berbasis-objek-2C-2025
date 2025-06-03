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
    print(f"Gaji {karyawan.nama}: Rp{karyawan.hitung_gaji():,.2f}")


while True:
    print("\nPilih tipe karyawan:")
    print("1. Karyawan Tetap")
    print("2. Karyawan Kontrak")
    print("0. Keluar")

    pilihan = int(input("Masukkan pilihan (0-2): "))

    if pilihan == 1:
        try:
            nama = input("Masukkan nama: ")
            gaji = float(input("Masukkan gaji bulanan: "))
            k = KaryawanTetap(nama, gaji)
            cetak_gaji(k)
        except ValueError:
            print("Input harus berupa angka.")
    elif pilihan == 2:
        try:
            nama = input("Masukkan nama: ")
            jam = float(input("Masukkan jumlah jam kerja: "))
            upah = float(input("Masukkan upah per jam: "))
            k = KaryawanKontrak(nama, jam, upah)
            cetak_gaji(k)
        except ValueError:
            print("Input harus berupa angka.")
    elif pilihan == 0:
        print("Program selesai. Terima kasih.")
        break
    else:
        print("Pilihan tidak valid. Coba lagi.")
