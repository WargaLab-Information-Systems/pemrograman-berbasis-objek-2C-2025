from abc import ABC, abstractmethod

class Karyawan(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def hitung_gaji(self):
        pass

class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji_pokok):
        super().__init__(nama)
        self.gaji_pokok = gaji_pokok

    def hitung_gaji(self):
        return self.gaji_pokok

class KaryawanKontrak(Karyawan):
    def __init__(self, nama, jam_kerja, upah_per_jam):
        super().__init__(nama)
        self.jam_kerja = jam_kerja
        self.upah_per_jam = upah_per_jam

    def hitung_gaji(self):
        return self.jam_kerja * self.upah_per_jam

def cetak_gaji(karyawan: Karyawan):
    print(f"Gaji {karyawan.nama} ({karyawan.__class__.__name__}) = Rp {karyawan.hitung_gaji():,.2f}")

def validasi_nama(prompt):
    while True:
        nama = input(prompt).strip()
        if nama != "" and all(c.isalpha() or c.isspace() for c in nama):
            return nama
        print("Nama harus hanya berisi huruf dan spasi, coba lagi.")

def validasi_float(prompt):
    while True:
        nilai = input(prompt).strip()
        if nilai.replace('.', '', 1).isdigit():
            val_float = float(nilai)
            if val_float >= 0:
                return val_float
        print("Input harus berupa angka positif, coba lagi.")

def main():
    daftar_karyawan = []

    while True:
        print("\n== Input Data Karyawan ==")
        print("1. Karyawan Tetap")
        print("2. Karyawan Kontrak")
        print("3. Selesai dan Tampilkan Gaji")
        pilihan = int(input("Pilih tipe karyawan (1/2/3): "))

        if pilihan == 1:
            nama = validasi_nama("Masukkan nama karyawan tetap: ")
            gaji_pokok = validasi_float("Masukkan gaji pokok: ")
            k = KaryawanTetap(nama, gaji_pokok)
            daftar_karyawan.append(k)

        elif pilihan == 2:
            nama = validasi_nama("Masukkan nama karyawan kontrak: ")
            jam_kerja = validasi_float("Masukkan jumlah jam kerja: ")
            upah_per_jam = validasi_float("Masukkan upah per jam: ")
            k = KaryawanKontrak(nama, jam_kerja, upah_per_jam)
            daftar_karyawan.append(k)
        elif pilihan == 3:
            print("\n== Daftar Gaji Karyawan ==")
            for karyawan in daftar_karyawan:
                cetak_gaji(karyawan)
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

main()