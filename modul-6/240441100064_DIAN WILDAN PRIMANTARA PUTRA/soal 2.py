from abc import ABC, abstractmethod

class Karyawan(ABC):
    def __init__(self, nama, departemen):
        self.nama = nama
        self.departemen = departemen

    @abstractmethod
    def hitung_gaji(self):
        pass

    def info(self):
        print(f"Nama: {self.nama}")
        print(f"Departemen: {self.departemen}")

class KaryawanTetap(Karyawan):
    def __init__(self, nama, departemen, gaji_pokok, tunjangan):
        super().__init__(nama, departemen)
        self.gaji_pokok = gaji_pokok
        self.tunjangan = tunjangan

    def hitung_gaji(self):
        return self.gaji_pokok + self.tunjangan

    def info(self):
        print("Jenis Karyawan: Karyawan Tetap")
        super().info()
        print(f"Gaji Pokok: {self.gaji_pokok}")
        print(f"Tunjangan: {self.tunjangan}")
        print(f"Total Gaji: {self.hitung_gaji()}")

class KaryawanKontrak(Karyawan):
    def __init__(self, nama, departemen, gaji_per_jam, jam_kerja):
        super().__init__(nama, departemen)
        self.gaji_per_jam = gaji_per_jam
        self.jam_kerja = jam_kerja

    def hitung_gaji(self):
        return self.gaji_per_jam * self.jam_kerja

    def info(self):
        print("Jenis Karyawan: Karyawan Kontrak")
        super().info()
        print(f"Gaji per Jam: {self.gaji_per_jam}")
        print(f"Jam Kerja: {self.jam_kerja}")
        print(f"Total Gaji: {self.hitung_gaji()}")

class ManajemenKaryawan:
    def __init__(self):
        self.daftar_karyawan = []

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_semua_karyawan(self):
        print("\n=== Daftar Karyawan ===")
        for karyawan in self.daftar_karyawan:
            karyawan.info()
            print("-" * 30)

def input_karyawan():
    manajer = ManajemenKaryawan()

    while True:
        print("\nTambah Karyawan Baru")
        jenis = input("Jenis Karyawan (Tetap/Kontrak): ").strip().lower()

        nama = input("Nama: ")
        departemen = input("Departemen: ")

        if jenis == "tetap":
            gaji_pokok = int(input("Gaji Pokok: "))
            tunjangan = int(input("Tunjangan: "))
            karyawan = KaryawanTetap(nama, departemen, gaji_pokok, tunjangan)

        elif jenis == "kontrak":
            gaji_per_jam = int(input("Gaji per Jam: "))
            jam_kerja = int(input("Jam Kerja: "))
            karyawan = KaryawanKontrak(nama, departemen, gaji_per_jam, jam_kerja)

        else:
            print("Jenis karyawan tidak valid. Coba lagi.")
            continue

        manajer.tambah_karyawan(karyawan)

        lagi = input("Tambah karyawan lagi? (y/n): ").strip().lower()
        if lagi != 'y':
            break

    manajer.tampilkan_semua_karyawan()

input_karyawan()