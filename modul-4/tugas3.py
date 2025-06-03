class Pasien:
    def __init__(self, nama, umur, keluhan):
        self.__nama = nama
        self.__umur = umur
        self.__keluhan = keluhan

    def get_nama(self):
        return self.__nama

    def get_umur(self):
        return self.__umur

    def get_keluhan(self):
        return self.__keluhan

    def __str__(self):
        return f"Nama: {self.__nama}, Umur: {self.__umur} tahun, Keluhan: {self.__keluhan}"


class Klinik:
    def __init__(self):
        self.daftar_pasien = []

    def tambah_pasien(self, pasien):
        self.daftar_pasien.append(pasien)
        print(f"Pasien '{pasien.get_nama()}' berhasil ditambahkan.")

    def tampilkan_semua_pasien(self):
        if not self.daftar_pasien:
            print("Belum ada data pasien.")
        else:
            print("\n=== Daftar Pasien Klinik ===")
            for i, pasien in enumerate(self.daftar_pasien, start=1):
                print(f"{i}. {pasien}")



def main():
    klinik = Klinik()

    while True:
        print("\n===== MENU KLINIK =====")
        print("1. Tambah Pasien")
        print("2. Tampilkan Semua Pasien")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == "1":
            nama = input("Masukkan nama pasien: ")
            umur_input = input("Masukkan umur pasien: ")
            keluhan = input("Masukkan keluhan pasien: ")

            if umur_input.isdigit():
                umur = int(umur_input)
                pasien = Pasien(nama, umur, keluhan)
                klinik.tambah_pasien(pasien)
            else:
                print("Umur harus berupa angka. Pasien tidak ditambahkan.")

        elif pilihan == "2":
            klinik.tampilkan_semua_pasien()

        elif pilihan == "3":
            print("Program selesai. Terima kasih.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")


if __name__ == "__main__":
    main()
