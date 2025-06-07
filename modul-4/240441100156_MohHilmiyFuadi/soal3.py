class Pasien:
    def __init__(self, nama, umur, keluhan, dokter):
        self.__nama = nama
        self.__umur = umur
        self.__keluhan = keluhan
        self.__dokter = dokter

    def get_nama(self):
        return self.__nama

    def get_umur(self):
        return self.__umur

    def get_keluhan(self):
        return self.__keluhan

    def get_dokter(self):
        return self.__dokter

    def set_nama(self, nama):
        self.__nama = nama

    def set_umur(self, umur):
        self.__umur = umur

    def set_keluhan(self, keluhan):
        self.__keluhan = keluhan

    def set_dokter(self, dokter):
        self.__dokter = dokter


class Klinik:
    def __init__(self):
        self.__daftar_pasien = []

    def tambah_pasien(self, nama, umur, keluhan, dokter):
        pasien = Pasien(nama, umur, keluhan, dokter)
        self.__daftar_pasien.append(pasien)
        print("Pasien berhasil ditambahkan.")

    def tampilkan_daftar_pasien(self):
        if not self.__daftar_pasien:
            print("Belum ada pasien yang terdaftar.")
        else:
            print("\nDaftar Pasien di Klinik:")
            for i, pasien in enumerate(self.__daftar_pasien, start=1):
                print(f"{i}. Nama: {pasien.get_nama()} | Umur: {pasien.get_umur()} | Keluhan: {pasien.get_keluhan()} | Dokter: {pasien.get_dokter()}")

    def tampilkan_pasien_berdasarkan_dokter(self, nama_dokter):
        pasien_dokter = [p for p in self.__daftar_pasien if p.get_dokter().lower() == nama_dokter.lower()]
        if not pasien_dokter:
            print(f"Tidak ada pasien untuk dokter {nama_dokter}.")
        else:
            print(f"\nPasien yang ditangani oleh Dokter {nama_dokter}:")
            for i, pasien in enumerate(pasien_dokter, start=1):
                print(f"{i}. Nama: {pasien.get_nama()} | Umur: {pasien.get_umur()} | Keluhan: {pasien.get_keluhan()}")

    def edit_pasien(self, index, nama_baru, umur_baru, keluhan_baru, dokter_baru):
        if 0 <= index < len(self.__daftar_pasien):
            pasien = self.__daftar_pasien[index]
            pasien.set_nama(nama_baru)
            pasien.set_umur(umur_baru)
            pasien.set_keluhan(keluhan_baru)
            pasien.set_dokter(dokter_baru)
            print("Data pasien berhasil diperbarui.")
        else:
            print("Index pasien tidak valid.")


def main():
    klinik = Klinik()

    while True:
        print("\n=== Menu Klinik ===")
        print("1. Tambah Pasien")
        print("2. Tampilkan Semua Pasien")
        print("3. Tampilkan Pasien Berdasarkan Dokter")
        print("4. Edit Data Pasien")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            nama = input("Masukkan nama pasien       : ")
            try:
                umur = int(input("Masukkan umur pasien       : "))
            except ValueError:
                print("Umur harus berupa angka!")
                continue
            keluhan = input("Masukkan keluhan pasien    : ")
            dokter = input("Masukkan nama dokter       : ")
            klinik.tambah_pasien(nama, umur, keluhan, dokter)

        elif pilihan == "2":
            klinik.tampilkan_daftar_pasien()

        elif pilihan == "3":
            dokter = input("Masukkan nama dokter: ")
            klinik.tampilkan_pasien_berdasarkan_dokter(dokter)

        elif pilihan == "4":
            klinik.tampilkan_daftar_pasien()
            index_input = input("Masukkan nomor pasien yang ingin diedit: ")
            if index_input.isdigit():
                index = int(index_input) - 1
                nama = input("Nama baru      : ")
                try:
                    umur = int(input("Umur baru      : "))
                except ValueError:
                    print("Umur harus angka!")
                    continue
                keluhan = input("Keluhan baru   : ")
                dokter = input("Dokter baru    : ")
                klinik.edit_pasien(index, nama, umur, keluhan, dokter)
            else:
                print("Input tidak valid.")

        elif pilihan == "5":
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
    #tambahkan tampil pasien berdasarkan dokter 
    # edit pasien