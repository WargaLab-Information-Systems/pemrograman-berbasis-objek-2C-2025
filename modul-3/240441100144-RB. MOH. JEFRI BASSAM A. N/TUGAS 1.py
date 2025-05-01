class karyawan:
    def __init__(self, nama, gaji, departemen):
        self.nama = nama
        self.gaji = gaji
        self.departemen = departemen

    def info(self):
        print(f"nama       : {self.nama}")
        print(f"gaji       : Rp{self.gaji}")
        print(f"departemen : {self.departemen}")

class Karyawan_Tetap(karyawan):
    def __init__(self, nama, gaji, departemen, tunjangan):
        super().__init__(nama, gaji, departemen)
        self.tunjangan = tunjangan
     
    def info(self):
        print("----- Data Karyawan Tetap -----")
        super().info()
        print(f"tunjangan  : Rp{self.tunjangan}")
        print()
    
class Karyawan_Harian(karyawan):
    def __init__(self, nama, gaji, departemen, jam_kerja):
        super().__init__(nama, gaji, departemen)
        self.jam_kerja = jam_kerja

    def info(self):
        print("----- Data Karyawan Harian -----")
        super().info()
        print(f"jam kerja  : {self.jam_kerja} jam/hari")
        print()

class manajemenKaryawan:
    def __init__(self):
        self.daftar_karyawan = []

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_semua_karyawan(self):
        if len(self.daftar_karyawan) == 0:
            print("\n----- Belum ada karyawan yang terdaftar dilist -----")
        else:
            print("\n----- DAFTAR KARYAWAN PT. UNIJOYO -----")
            for karyawan in self.daftar_karyawan:
                karyawan.info()

def menu_input_karyawan(manajemen):
    while True:
        print("\n------- PT. UNIJOYO -------")
        print("Pilih menu di bawah ini:")
        print("1. Tambah Karyawan Tetap")
        print("2. Tambah Karyawan Harian")
        print("3. Tampilkan Semua Karyawan")
        print("4. Keluar")

        pilihan = input("masukkan pilihan (1-4): ")

        if pilihan == "1":
            print("\n--- Input Karyawan Tetap ---")
            nama = input("Nama : ")
            gaji = int(input("Gaji : "))
            departemen = input("Departemen : ")
            tunjangan = int(input("Tunjangan : "))
            karyawan = Karyawan_Tetap(nama, gaji, departemen, tunjangan)
            manajemen.tambah_karyawan(karyawan)
            print("\n-- Data karyawan tetap berhasil diinput!! --")

        elif pilihan == "2":
            print("\n--- Input Karyawan Harian ---")
            nama = input("Nama : ")
            gaji = int(input("Gaji per hari : "))
            departemen = input("Departemen : ")
            
            while True:
                jam_kerja = float(input("Jam kerja per hari : "))
                if jam_kerja > 24:
                    print("\n--- masukkan diantara 0-24 ---\n")

                elif jam_kerja <= 24:
                    break

            karyawan = Karyawan_Harian(nama, gaji, departemen, jam_kerja)
            manajemen.tambah_karyawan(karyawan)
            print("\n-- Data karyawan harian berhasil diinput!! --")

        elif pilihan == "3":
            manajemen.tampilkan_semua_karyawan()

        elif pilihan == "4":
            print("\n----- Terima kasih!!!!! -----\n")
            break

        else:
            print("\n----- pilihan tidak valid, silahkan coba lagi -----\n")
            pass

manajemen = manajemenKaryawan()
menu_input_karyawan(manajemen)
