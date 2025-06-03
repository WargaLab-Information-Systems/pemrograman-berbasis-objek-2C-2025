class Pasien:
    def __init__ (self, nama, umur, keluhan):
        self.__nama = nama
        self.__umur = umur
        self.__keluhan = keluhan

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def umur(self):
        return self.__umur

    @umur.setter
    def umur(self, value):
        self.__umur = value

    @property
    def keluhan(self):
        return self.__keluhan

    @keluhan.setter
    def keluhan(self, value):
        self.__keluhan = value

class Klinik:
    def __init__(self):
        self.daftar_pasien = []

    def tambah_pasien(self, nama, umur, keluhan):
        pasien_baru = Pasien(nama, umur, keluhan)
        self.daftar_pasien.append(pasien_baru)
        print(f"Pasien dengan nama {nama} berhasil ditambahkan")

    def tampilkan_pasien(self):
        print("\nDaftar Pasien di Klinik Telang")
        if not self.daftar_pasien:
            print("Belum ada pasien.")
        for i, pasien in enumerate(self.daftar_pasien, start=1):
            print(f"{i}. Nama    : {pasien.nama}")
            print(f"   Umur    : {pasien.umur}")
            print(f"   Keluhan : {pasien.keluhan}")
            print("-" * 40)

    def ubah_pasien(self, nomor, nama_baru, umur_baru, keluhan_baru):
        if 1 <= nomor <= len(self.daftar_pasien):
            pasien = self.daftar_pasien[nomor-1]
            pasien.nama = nama_baru
            pasien.umur = umur_baru
            pasien.keluhan = keluhan_baru
            print("Data pasien berhasil diubah.")
        else:
            print("Nomor pasien tidak valid.")

    def hapus_pasien(self, nomor):
        if 1 <= nomor <= len(self.daftar_pasien):
            pasien = self.daftar_pasien.pop(nomor-1)
            print(f"Pasien '{pasien.nama}' berhasil dihapus.")
        else:
            print("Nomor pasien tidak valid.")

class main:
    def __init__(self):
        self.klinik = Klinik()
        self.menu()

    def menu(self):
        while True:
            print("\n===== Klinik Telang =====")
            print("1. Tambah Pasien")
            print("2. Lihat Semua Pasien")
            print("3. Ubah Data Pasien")
            print("4. Hapus Pasien")
            print("5. Keluar")
            pilihan = input("Pilih Menu: ")

            if pilihan == "1":
                nama = input("Masukkan Nama Pasien: ")
                umur = input("Masukkan Umur Pasien: ")
                keluhan = input("Masukkan Keluhan Pasien: ")
                self.klinik.tambah_pasien(nama, umur, keluhan)
            elif pilihan == "2":
                self.klinik.tampilkan_pasien()
            elif pilihan == "3":
                self.klinik.tampilkan_pasien()
                nomor = int(input("Masukkan nomor pasien yang ingin diubah: "))
                nama_baru = input("Masukkan nama baru: ")
                umur_baru = input("Masukkan umur baru: ")
                keluhan_baru = input("Masukkan keluhan baru: ")
                self.klinik.ubah_pasien(nomor, nama_baru, umur_baru, keluhan_baru)
            elif pilihan == "4":
                self.klinik.tampilkan_pasien()
                nomor = int(input("Masukkan nomor pasien yang ingin dihapus: "))
                self.klinik.hapus_pasien(nomor)
            elif pilihan == "5":
                print("Terima kasih!")
                break
            else:
                print("Pilihan tidak valid.")

main()