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
    print(f"Gaji {karyawan.nama} ({karyawan.__class__.__name__}): Rp{int(karyawan.hitung_gaji()):,}")

def main():
    daftar_karyawan = []

    while True:
        print("\nPilih jenis karyawan:")
        print("1. Karyawan Tetap")
        print("2. Karyawan Kontrak")
        print("3. Tampilkan Semua Gaji")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan (1-4): ")

        if pilihan == "1":
            nama = input("Nama: ")
            gaji_bulanan = float(input("Gaji bulanan: "))
            karyawan = KaryawanTetap(nama, gaji_bulanan)
            daftar_karyawan.append(karyawan)

        elif pilihan == "2":
            nama = input("Nama: ")
            jam_kerja = float(input("Jumlah jam kerja: "))
            upah_per_jam = float(input("Upah per jam: "))
            karyawan = KaryawanKontrak(nama, jam_kerja, upah_per_jam)
            daftar_karyawan.append(karyawan)

        elif pilihan == "3":
            print("\nDaftar Gaji Karyawan:")
            for karyawan in daftar_karyawan:
                cetak_gaji(karyawan)

        elif pilihan == "4":
            print("Terima kasih!")
            break

        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
