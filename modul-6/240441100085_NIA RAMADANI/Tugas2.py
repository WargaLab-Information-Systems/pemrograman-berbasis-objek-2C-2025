from abc import ABC, abstractmethod

class Karyawan(ABC):
    def __init__(self, id_karyawan, nama, bagian):
        self.id_karyawan = id_karyawan
        self.nama = nama
        self.bagian = bagian

    @abstractmethod
    def hitung_gaji(self):
        pass

    @abstractmethod
    def tampilkan_gaji(self):
        pass

class KaryawanTetap(Karyawan):
    def __init__(self, id_karyawan, nama, bagian, gaji_pokok, tunjangan, potongan=0, bonus=0):
        super().__init__(id_karyawan, nama, bagian)
        self.gaji_pokok = gaji_pokok
        self.tunjangan = tunjangan
        self.potongan = potongan
        self.bonus = bonus

    def hitung_gaji(self):
        return self.gaji_pokok + self.tunjangan - self.potongan + self.bonus

    def tampilkan_gaji(self):
        print(f"ID Karyawan     : {self.id_karyawan}")
        print(f"Nama Karyawan   : {self.nama}")
        print(f"Bagian          : {self.bagian}")
        print(f"Tipe Karyawan   : Tetap")
        print(f"Gaji Pokok      : Rp {self.gaji_pokok:,.2f}")
        print(f"Tunjangan       : Rp {self.tunjangan:,.2f}")
        print(f"Potongan        : Rp {self.potongan:,.2f}")
        print(f"Bonus           : Rp {self.bonus:,.2f}")
        print(f"Gaji Bersih     : Rp {self.hitung_gaji():,.2f}")
        print("-" * 40)

class KaryawanKontrak(Karyawan):
    def __init__(self, id_karyawan, nama, bagian, jam_kerja, upah_per_jam, potongan=0, bonus=0):
        super().__init__(id_karyawan, nama, bagian)
        self.jam_kerja = jam_kerja
        self.upah_per_jam = upah_per_jam
        self.potongan = potongan
        self.bonus = bonus

    def hitung_gaji(self):
        return (self.jam_kerja * self.upah_per_jam) - self.potongan + self.bonus

    def tampilkan_gaji(self):
        print(f"ID Karyawan     : {self.id_karyawan}")
        print(f"Nama Karyawan   : {self.nama}")
        print(f"Bagian          : {self.bagian}")
        print(f"Tipe Karyawan   : Kontrak")
        print(f"Jam Kerja       : {self.jam_kerja} jam")
        print(f"Upah per Jam    : Rp {self.upah_per_jam:,.2f}")
        print(f"Potongan        : Rp {self.potongan:,.2f}")
        print(f"Bonus           : Rp {self.bonus:,.2f}")
        print(f"Gaji Bersih     : Rp {self.hitung_gaji():,.2f}")

        estimasi_jam_bulanan = 200  
        estimasi_gaji_bulanan = (self.upah_per_jam * estimasi_jam_bulanan) + self.bonus - self.potongan
        print(f"Estimasi Gaji 1 Bulan (200 jam): Rp {estimasi_gaji_bulanan:,.2f}")
        print("-" * 40)

def input_nama():
    while True:
        nama = input("Masukkan nama karyawan (tanpa angka): ")
        if any(char.isdigit() for char in nama):
            print("Nama tidak boleh mengandung angka.")
        elif len(nama.strip()) == 0:
            print("Nama tidak boleh kosong.")
        else:
            return nama

def main():
    daftar_karyawan = []

    while True:
        print("\n--- Sistem Penggajian Karyawan ---")
        print("1. Tambah Karyawan Tetap")
        print("2. Tambah Karyawan Kontrak")
        print("3. Lihat Daftar Gaji")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            id_karyawan = input("ID Karyawan: ")
            nama = input_nama()
            bagian = input("Bagian/Jabatan: ")
            gaji_pokok = float(input("Gaji Pokok: "))
            tunjangan = float(input("Tunjangan: "))
            potongan = float(input("Potongan (jika ada): ") or "0")
            bonus = float(input("Bonus (jika ada): ") or "0")

            karyawan = KaryawanTetap(id_karyawan, nama, bagian, gaji_pokok, tunjangan, potongan, bonus)
            daftar_karyawan.append(karyawan)
            print("Karyawan Tetap berhasil ditambahkan.")

        elif pilihan == "2":
            id_karyawan = input("ID Karyawan: ")
            nama = input_nama()
            bagian = input("Bagian/Jabatan: ")
            jam_kerja = int(input("Jam Kerja: "))
            upah_per_jam = float(input("Upah per Jam: "))
            potongan = float(input("Potongan (jika ada): ") or "0")
            bonus = float(input("Bonus (jika ada): ") or "0")

            karyawan = KaryawanKontrak(id_karyawan, nama, bagian, jam_kerja, upah_per_jam, potongan, bonus)
            daftar_karyawan.append(karyawan)
            print("Karyawan Kontrak berhasil ditambahkan.")

        elif pilihan == "3":
            if not daftar_karyawan:
                print("Belum ada data karyawan.")
            else:
                print("\n--- Daftar Gaji Karyawan ---")
                for karyawan in daftar_karyawan:
                    karyawan.tampilkan_gaji()

        elif pilihan == "4":
            print("Program selesai. Terima kasih.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
