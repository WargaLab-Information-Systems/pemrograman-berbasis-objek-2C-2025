class Karyawan:
    def __init__(self, nama, gaji, departemen):
        self.nama = nama
        self.gaji = gaji
        self.departemen = departemen

    def info(self):
        print(f"Nama: {self.nama}")
        print(f"Gaji: {self.gaji}")
        print(f"Departemen: {self.departemen}")

class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji, departemen, tunjangan):
        super().__init__(nama, gaji, departemen)
        self.tunjangan = tunjangan

    def info(self):
        super().info()
        print(f"Tunjangan: {self.tunjangan}")
        print("Status: Karyawan Tetap\n")

class KaryawanHarian(Karyawan):
    def __init__(self, nama, gaji, departemen, jam_kerja):
        super().__init__(nama, gaji, departemen)
        self.jam_kerja = jam_kerja

    def info(self):
        super().info()
        print(f"Jam Kerja: {self.jam_kerja} jam/hari")
        print("Status: Karyawan Harian\n")

class ManajemenKaryawan:
    def __init__(self):
        self.daftar_karyawan = []

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_karyawan(self):
        print("\n=== Daftar Semua Karyawan ===")
        if not self.daftar_karyawan:
            print("Karyawan belum ada")
        else:
            for i, karyawan in enumerate(self.daftar_karyawan, start=1):
                print(f"\nKaryawan {i}:")
                karyawan.info()

def input_karyawan(manajemen):
    while True:
        print("Tambah Karyawan")
        jenis = input("Karyawan Tetap(1) atau Karyawan Harian(2): ") 

        nama = input("Nama: ")
        gaji = int(input("Gaji: "))
        departemen = input("Departemen: ")

        if jenis == "1":
            tunjangan = int(input("Tunjangan: "))
            karyawan = KaryawanTetap(nama, gaji, departemen, tunjangan)
        elif jenis == "2":
            jam_kerja = int(input("Jam Kerja: "))
            karyawan = KaryawanHarian(nama, gaji, departemen, jam_kerja)
        else:
            print("Input salah")
            continue
        
        manajemen.tambah_karyawan(karyawan)

        lanjut = input("Tambah karyawan lagi? (ya/tidak): ")
        if lanjut != "ya":
            break

def main():
    manajemen = ManajemenKaryawan()
    input_karyawan(manajemen)
    manajemen.tampilkan_karyawan()

if __name__ == "__main__":
    main()