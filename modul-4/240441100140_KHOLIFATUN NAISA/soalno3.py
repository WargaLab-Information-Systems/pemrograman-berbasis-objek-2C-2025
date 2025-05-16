class Pasien:
    def __init__(self, nama, umur, keluhan):
        self.__nama = nama
        self.__umur = umur
        self.__keluhan = keluhan
    @property
    def nama(self):
        return self.__nama
    @property
    def umur(self):
        return self.__umur
    @property
    def keluhan(self):
        return self.__keluhan
    @nama.setter
    def nama(self, nama):
        self.__nama = nama
    @keluhan.setter
    def keluhan(self, keluhan):
        self.__keluhan = keluhan

class Klinik:
    def __init__(self):
        self.daftar_pasien = []
    def tambah_pasien(self, nama, umur, keluhan):
        pasien_baru = Pasien(nama, umur, keluhan)
        self.daftar_pasien.append(pasien_baru)
    def tampilkan_semua_pasien(self):
        if not self.daftar_pasien:
            print("Tidak ada pasien dalam daftar.")
        else:
            for i, pasien in enumerate(self.daftar_pasien, start=1):
                print(f"{i}. Nama: {pasien.nama}, Umur: {pasien.umur}, Keluhan: {pasien.keluhan}")
    def edit_pasien(self):
        self.tampilkan_semua_pasien()
        if not self.daftar_pasien:
            return
        nomor = int(input("Masukkan nomor pasien yang ingin diedit: ")) - 1
        if 0 <= nomor < len(self.daftar_pasien):
            pasien = self.daftar_pasien[nomor]
            keluhan_baru = input("Masukkan keluhan baru: ")
            if keluhan_baru:
                pasien.keluhan = keluhan_baru
            print("Data pasien berhasil diperbarui.")
        else:
            print("Nomor pasien tidak ditemukan.")
    def hapus_pasien(self):
        self.tampilkan_semua_pasien()
        if not self.daftar_pasien:
            return
        nomor = int(input("Masukkan nomor pasien yang ingin dihapus: ")) - 1
        if 0 <= nomor < len(self.daftar_pasien):
            self.daftar_pasien.pop(nomor)
            print("Pasien berhasil dihapus.")
        else:
            print("Nomor pasien tidak ditemukan.")


def main():
    klinik = Klinik()
    while True:
        print("\nMenu Klinik")
        print("1. Tambah Pasien")
        print("2. Edit Pasien")
        print("3. Delete Pasien")
        print("4. Tampilkan Semua Pasien")
        print("5. Keluar")
        pilihan = int(input("Pilih menu: "))
        if pilihan == 1:
            nama = input("Masukkan nama pasien: ")
            umur = int(input("Masukkan umur pasien: "))
            keluhan = input("Masukkan jenis keluhan pasien: ")
            klinik.tambah_pasien(nama, umur, keluhan)
            print("Pasien berhasil ditambahkan.")
        elif pilihan == 2:
            klinik.edit_pasien()
        elif pilihan == 3:
            klinik.hapus_pasien()
        elif pilihan == 4:
            klinik.tampilkan_semua_pasien()
        elif pilihan == 5:
            print("Terima kasih telah menggunakan layanan Klinik.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

main()

#edit no pasien, keluhan, delete pasien (salah satu)