from abc import ABC, abstractmethod

class Karyawan(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def hitung_gaji(self):
        pass

class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji_pokok, tunjangan):
        super().__init__(nama)
        self.gaji_pokok = gaji_pokok
        self.tunjangan = tunjangan

    def hitung_gaji(self):
        return self.gaji_pokok + self.tunjangan

class KaryawanKontrak(Karyawan):
    def __init__(self, nama, jam_kerja, upah_per_jam):
        super().__init__(nama)
        self.jam_kerja = jam_kerja
        self.upah_per_jam = upah_per_jam

    def hitung_gaji(self):
        return self.jam_kerja * self.upah_per_jam

def cetak_gaji(karyawan):
    print(f"Gaji {karyawan.nama} ({type(karyawan).__name__}): Rp {karyawan.hitung_gaji():,.2f}")    

def main():
    while True:
        print("\nPilihlah jenis karyawan:")
        print("1. Karyawan Tetap")
        print("2. Karyawan Kontrak")

        try:
            pilihan = int(input("Masukkan pilihan: "))
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")
            continue

        if pilihan == 1:
            nama = input("Masukkan nama karyawan: ")
            try:
                gaji_pokok = float(input("Masukkan gaji pokok: "))
                tunjangan = float(input("Masukkan tunjangan: "))
            except ValueError:
                print("Input tidak valid. Harap masukkan angka untuk gaji/tunjangan.")
                continue
            karyawan = KaryawanTetap(nama, gaji_pokok, tunjangan)
            cetak_gaji(karyawan)
        elif pilihan == 2:
            nama = input("Masukkan nama karyawan: ")
            try:
                jam_kerja = float(input("Masukkan jam kerja: "))
                upah_per_jam = float(input("Masukkan upah per jam: "))
            except ValueError:
                print("Input tidak valid. Harap masukkan angka untuk jam kerja/upah.")
                continue
            karyawan = KaryawanKontrak(nama, jam_kerja, upah_per_jam)
            cetak_gaji(karyawan)
        else:
            print("Pilihan tidak valid.")

        n = input("Mau hitung gaji lagi? (y/n): ").lower()
        if n != "y":
            break

if __name__ == "__main__":
    main()