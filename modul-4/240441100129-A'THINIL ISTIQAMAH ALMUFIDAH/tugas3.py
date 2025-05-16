class Pasien:
    def __init__(self, nama, umur, keluhan, ruangan=None):
        self.__nama = nama
        self.__umur = umur
        self.__keluhan = keluhan
        self.__ruangan = ruangan  

    @property
    def info(self):
        ruangan_info = f", Ruangan: {self.__ruangan}" if self.__ruangan else ""
        return f"Nama: {self.__nama}, Umur: {self.__umur}, Keluhan: {self.__keluhan}{ruangan_info}"


class Klinik:
    def __init__(self):
        self.__daftar_pasien = []

    def tambah_pasien(self, nama, umur, keluhan, ruangan=None):
        pasien_baru = Pasien(nama, umur, keluhan, ruangan)
        self.__daftar_pasien.append(pasien_baru)
        print("Pasien berhasil ditambahkan.")

    def tampilkan_semua_pasien(self):
        if not self.__daftar_pasien:
            print("Belum ada data pasien.")
        else:
            print("\nDaftar Pasien:")
            for i, pasien in enumerate(self.__daftar_pasien, 1):
                print(f"{i}. {pasien.info}")


def main():
    klinik = Klinik()

    while True:
        print("\n=== MENU KLINIK ===")
        print("1. Tambah Pasien")
        print("2. Tampilkan Semua Pasien")
        print("3. Keluar")
        pilihan = input("Pilih menu (1-3): ")

        if pilihan == '1':
            nama = input("Masukkan nama pasien: ")
            try:
                umur = int(input("Masukkan umur pasien: "))
                keluhan = input("Masukkan keluhan pasien: ")
                ruangan = input("Masukkan nama ruangan: ")
                klinik.tambah_pasien(nama, umur, keluhan, ruangan)
            except ValueError:
                print("Umur harus berupa angka.")

        elif pilihan == '2':
            klinik.tampilkan_semua_pasien()

        elif pilihan == '3':
            print("Terima kasih. Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
#  nambah ruangan