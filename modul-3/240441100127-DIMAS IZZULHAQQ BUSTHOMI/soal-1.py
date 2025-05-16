class Karyawan:
    def __init__(self, nama, gaji, departemen):
        self.nama = nama
        self.gaji = gaji
        self.departemen = departemen
    
    def info(self):
        print(f"Nama       : {self.nama}")
        print(f"Gaji       : {self.gaji}")
        print(f"Departemen : {self.departemen}")

class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji, departemen, tunjangan):
        super().__init__(nama, gaji, departemen)
        self.tunjangan = tunjangan

    def info(self):
        print("Karyawan Tetap -")
        super().info()
        print(f"Tunjangan  : {self.tunjangan}")
        print("-----" * 10)

class KaryawanHarian(Karyawan):
    def __init__(self, nama, gaji, departemen, jam_kerja):
        super().__init__(nama, gaji, departemen)
        self.jam_kerja = jam_kerja

    def info(self):
        print("Karyawan Harian - ")
        super().info()
        print(f"Jam kerja  : {self.jam_kerja} jam perhari.")
        print("-----" * 10)

class ManajemenKaryawan:
    def __init__(self):
        self.daftar_karyawan = []

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)
    
    def tampilkan_semua_karyawan(self):
        for karyawan in self.daftar_karyawan:
            karyawan.info()

manajemen = ManajemenKaryawan()

while True:
    print("Pilih menu:\n 1. Tambahkan Karyawan Tetap\n 2. Tambahkan Karyawan Harian\n 3. Tampilkan Semua Data Karyawan\n 4. Keluar")
    print("-----" * 10)
    pilih = input("Masukkan : ")

    if pilih == "1":
        print("-----" * 10)
        nama = input("Masukkan nama : ")
        gaji = input("Masukkan gaji : ")
        print("-----" * 8)
        print(" 1. Keuangan\n 2. Pemasaran\n 3. Produksi\n 4. Operasional")
        print("-----" * 8)
        departemen = input("Pilih departemen : ")
        print("-----" * 8)
        if departemen == "1":
            departemen = "Keuangan"
        elif departemen == "2":
            departemen = "Pemasaran"
        elif departemen == "3":
            departemen = "Produksi"
        elif departemen == "4":
            departemen = "Operasional"

        tunjangan = input("Masukkan tunjangan : ")
        print("-----" * 8)

        karyawan = KaryawanTetap(nama, gaji, departemen, tunjangan)
        manajemen.tambah_karyawan(karyawan)
    
    elif pilih == "2":
        print("-----" * 10)
        nama = input("Masukkan nama : ")
        gaji = input("Masukkan gaji : ")
        print("-----" * 8)
        print(" 1. Keuangan\n 2. Pemasaran\n 3. Produksi\n 4. Operasional")
        print("-----" * 8)
        departemen = input("Pilih departemen : ")
        print("-----" * 8)
        if departemen == "1":
            departemen = "Keuangan"
        elif departemen == "2":
            departemen = "Pemasaran"
        elif departemen == "3":
            departemen = "Produksi"
        elif departemen == "4":
            departemen = "Operasional"

        jam_kerja = input("Masukkan jam kerja (perhari) : ")
        print("-----" * 8)
    
        karyawan = KaryawanHarian(nama, gaji, departemen, jam_kerja)
        manajemen.tambah_karyawan(karyawan)

    elif pilih == "3":
        print("-----" * 10)
        print("Daftar Karyawan : ")
        manajemen.tampilkan_semua_karyawan()

    elif pilih == "4":
        print("Terimakasih...")
        break


