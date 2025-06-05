class Pasien:
    def __init__(self, nama, umur, keluhan):
        self.__nama = nama
        self.__umur = umur
        self.__keluhan = keluhan

    # Getter dan Setter Nama
    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, nama_baru):
        self.__nama = nama_baru

    # Getter dan Setter Umur
    @property
    def umur(self):
        return self.__umur

    @umur.setter
    def umur(self, umur_baru):
        if umur_baru > 0:
            self.__umur = umur_baru
        else:
            print("Umur harus lebih dari 0")

    # Getter dan Setter Keluhan
    @property
    def keluhan(self):
        return self.__keluhan

    @keluhan.setter
    def keluhan(self, keluhan_baru):
        self.__keluhan = keluhan_baru

    def tampilkan(self):
        print(f"Nama     : {self.__nama}")
        print(f"Umur     : {self.__umur}")
        print(f"Keluhan  : {self.__keluhan}")
        print("-" * 30)


class Klinik:
    def __init__(self):
        self.daftar_pasien = []

    def tambah_pasien(self, pasien):
        self.daftar_pasien.append(pasien)
        print("Pasien berhasil ditambahkan.")

    def tampilkan_pasien(self):
        if not self.daftar_pasien:
            print("Belum ada data pasien.")
        else:
            print("\nDaftar Pasien Klinik:")
            for pasien in self.daftar_pasien:
                pasien.tampilkan()


def main():
    klinik = Klinik()

    while True:
        print("\nMenu:")
        print("1. Tambah Pasien")
        print("2. Tampilkan Seluruh Pasien")
        print("3. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama = input("Masukkan Nama Pasien: ")
            try:
                umur = int(input("Masukkan Umur Pasien: "))
            except ValueError:
                print("Umur harus berupa angka.")
                continue
            keluhan = input("Masukkan Keluhan Pasien: ")
            pasien_baru = Pasien(nama, umur, keluhan)
            klinik.tambah_pasien(pasien_baru)

        elif pilihan == "2":
            klinik.tampilkan_pasien()

        elif pilihan == "3":
            print("Terima kasih telah menggunakan sistem Klinik.")
            break

        else:
            print("Pilihan tidak valid.")

main()