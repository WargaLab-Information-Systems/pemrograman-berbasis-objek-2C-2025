class Pasien:
    def __init__(self, nama, umur, keluhan):
        self.__nama = nama  
        self.__umur = umur
        self.__keluhan = keluhan 

    @property
    def nama(self):
        return self.__nama
    
    @nama.setter
    def nama(self, namabaru):
        self.__nama = namabaru
    
    @property
    def umur(self):
        return self.__umur
    
    @umur.setter
    def umur(self, umurbaru):
        self.__umur = umurbaru
    
    @property
    def keluhan(self):
        return self.__keluhan

    @keluhan.setter
    def keluhan(self, keluhanbaru):
        self.__keluhan = keluhanbaru


class Klinik:
    daftar_pasien = []

    def tambah_pasien(self, pasien):
        self.daftar_pasien.append(pasien)

    def cari_pasien(self, nama):
        for pasien in self.daftar_pasien:
            if pasien.nama == nama:
                return pasien
        return None

    def update_pasien(self):
        print("\n --- Ubah Data Pasien ---")
        nama_pasien = input("Masukkan nama pasien yang ingin diubah data : ")
        pasien = self.cari_pasien(nama_pasien)

        if pasien:
            print("--- Data Lama ---")
            print("Nama    : ", pasien.nama)
            print("Umur    : ", pasien.umur, "tahun")
            print("Keluhan : ", pasien.keluhan)
            print("-" * 30)

            namabaru = input("Masukkan nama baru    : ")
            umurbaru = int(input("Masukkan umur baru    : "))
            keluhanbaru = input("Masukkan keluhan baru : ")

            pasien.nama = namabaru
            pasien.umur = umurbaru
            pasien.keluhan = keluhanbaru

            print("\n --- data pasien berhasil diubah --- ")
        else:
            print("\n --- pasien tidak ditemukan ---")

    def tampilkan_pasien(self):
        if len(self.daftar_pasien) == 0:
            print("\n --- tidak ada pasien yang terdaftar --- ")
        else:
            print("\n --- Daftar Data Pasien Klinik UTM ---")
            index = 1
            for pasien in self.daftar_pasien:
                print(f"Pasien ke-{index}")
                print("Nama    : ", pasien.nama)
                print("Umur    : ", pasien.umur,"tahun")
                print("Keluhan : ", pasien.keluhan)
                print("-" * 30)
                index += 1


def main():
    klinik = Klinik()

    while True:
        print("\n === Menu Klinik UTM ===")
        print("1. Tambah Pasien")
        print("2. Ubah Data Pasien")
        print("3. Cari Pasien")
        print("4. Tampilkan Daftar Pasien")
        print("5. Keluar")

        pilihan = input("Pilih opsi (1-5): ")

        if pilihan == "1":
            print("\n --- Input Data Pasien ---")
            nama = input("Masukkan nama pasien    : ")
            umur = int(input("Masukkan umur pasien    : "))
            keluhan = input("Masukkan keluhan pasien : ")

            pasien = Pasien(nama, umur, keluhan)
            klinik.tambah_pasien(pasien)
            print("\n --- Pasien berhasil ditambahkan --- ")

        elif pilihan == "2":
            klinik.update_pasien()

        elif pilihan == "3":
            print("\n --- Cari Pasien ---")
            nama_cari = input("Masukkan nama pasien yang dicari: ")
            pasien = klinik.cari_pasien(nama_cari)
            if pasien:
                print("\n--- Data Ditemukan ---")
                print("Nama    : ", pasien.nama)
                print("Umur    : ", pasien.umur, "tahun")
                print("Keluhan : ", pasien.keluhan)
            else:
                print("\n --- Pasien tidak ditemukan ---")

        elif pilihan == "4":
            klinik.tampilkan_pasien()

        elif pilihan == "5":
            print("\n=== Terima kasih ===")
            print("=== Klinik UTM ===")
            break

        else:
            print("\n -- Pilihan tidak valid. Silakan pilih lagi --")


main()

