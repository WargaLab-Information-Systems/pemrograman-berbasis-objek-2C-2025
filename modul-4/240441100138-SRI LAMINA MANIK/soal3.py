class Pasien:
    def __init__(self, nama, umur, keluhan):
        self.__nama = nama
        self.__umur = umur
        self.__keluhan = keluhan

    def get_info(self):
        return f"Nama: {self.__nama}, Umur: {self.__umur}, Keluhan: {self.__keluhan}"

    def get_nama(self):
        return self.__nama


class Klinik:
    def __init__(self):
        self.pasien_list = []

    def tambah_pasien(self, pasien):
        self.pasien_list.append(pasien)
        print(" Pasien berhasil ditambahkan.")

    def tampilkan_pasien(self):
        if not self.pasien_list:
            print(" Belum ada pasien.")
        else:
            print("\n DAFTAR NAMA PASIEN:")
            for i, p in enumerate(self.pasien_list):                                    #index (nomor urutan) dan juga data pasien-nya.
                print(f"{i+1}. {p.get_info()}")

    def cari_pasien(self, nama_dicari):
        ditemukan = False
        for p in self.pasien_list:
            if nama_dicari.lower() in p.get_nama().lower():
                print(" Pasien ditemukan:")
                print(p.get_info())
                ditemukan = True
        if not ditemukan:
            print(" Pasien tidak ditemukan.")

    def hapus_pasien(self):
        self.tampilkan_pasien()
        if not self.pasien_list:
            return
        try:
            index = int(input("\nMasukkan nomor pasien yang ingin dihapus: ")) - 1
            if 0 <= index < len(self.pasien_list):
                pasien = self.pasien_list.pop(index)
                print(f" Pasien '{pasien.get_nama()}' berhasil dihapus.")
            else:
                print(" Nomor tidak valid.")
        except:
            print(" Input harus berupa angka.")


# Program utama
klinik = Klinik()

while True:
    print("\n=== MENU KLINIK ===")
    print("1. Tambah Pasien")
    print("2. Tampilkan Semua Pasien")
    print("3. Cari Pasien")
    print("4. Hapus Pasien")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        nama = input("Masukkan Nama Pasien: ")
        try:
            umur = int(input("Masukkan Umur Pasien: "))
        except:
            print(" Umur harus berupa angka.")
            continue
        keluhan = input("Masukkan Keluhan Pasien: ")
        pasien_baru = Pasien(nama, umur, keluhan)
        klinik.tambah_pasien(pasien_baru)

    elif pilihan == "2":
        klinik.tampilkan_pasien()

    elif pilihan == "3":
        nama_cari = input("Masukkan nama pasien yang ingin dicari: ")
        klinik.cari_pasien(nama_cari)

    elif pilihan == "4":
        klinik.hapus_pasien()

    elif pilihan == "5":
        print(" Terima kasih telah menggunakan sistem klinik.")
        break

    else:
        print(" Pilihan tidak valid.")
