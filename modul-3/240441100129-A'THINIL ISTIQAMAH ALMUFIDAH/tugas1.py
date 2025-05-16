class Karyawan:
    def __init__(self, nama, gaji, departemen):
        self.nama = nama
        self.gaji = gaji
        self.departemen = departemen

    def info(self):
        return f"Nama: {self.nama}, Gaji: {self.gaji}, Departemen: {self.departemen}"

class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji, departemen, tunjangan):
        super().__init__(nama, gaji, departemen)
        self.tunjangan = tunjangan

    def info(self):
        return f"{super().info()}, Tunjangan: {self.tunjangan}"

class KaryawanHarian(Karyawan):
    def __init__(self, nama, gaji, departemen, jam_kerja):
        super().__init__(nama, gaji, departemen)
        self.jam_kerja = jam_kerja

    def info(self):
        return f"{super().info()}, Jam Kerja per Hari: {self.jam_kerja}"

class ManajemenKaryawan:
    def __init__(self):
        self.karyawans = []

    def tambah_karyawan(self, karyawan):
        self.karyawans.append(karyawan)

    def tampilkan_semua_karyawan(self):
        print("\nData Semua Karyawan:")
        for idx, karyawan in enumerate(self.karyawans, 1):
            print(f"{idx}. {karyawan.info()}")

def input_angka(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Input harus berupa angka bulat. Silakan coba lagi.")

def main():
    manajemen = ManajemenKaryawan()
    while True:
        tipe = input("Tambah karyawan Tetap atau Harian? (T/H, '0' untuk selesai): ").strip().upper()
        if tipe == '0':
            break
        if tipe not in ('T', 'H'):
            print("Pilihan tidak valid, masukkan 'T', 'H', atau '0'.")
            continue

        nama = input("Nama karyawan: ")
        gaji = input_angka("Gaji: ")
        dept = input("Departemen: ")

        if tipe == 'T':
            tunjangan = input_angka("Tunjangan: ")
            karyawan = KaryawanTetap(nama, gaji, dept, tunjangan)
        else:
            jam_kerja = input_angka("Jam kerja per hari: ")
            karyawan = KaryawanHarian(nama, gaji, dept, jam_kerja)

        manajemen.tambah_karyawan(karyawan)
        print("Karyawan berhasil ditambahkan!\n")

    manajemen.tampilkan_semua_karyawan()

if __name__ == '__main__':
    main()
