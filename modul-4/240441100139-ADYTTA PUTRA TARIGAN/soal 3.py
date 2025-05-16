class Pasien:
    def __init__(self, nama, umur, keluhan, ruangan="Belum ditentukan"):
        self.__nama = nama
        self.__umur = umur
        self.__keluhan = keluhan
        self.__ruangan = ruangan

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, nama_baru):
        self.__nama = nama_baru

    @property
    def umur(self):
        return self.__umur

    @umur.setter
    def umur(self, umur_baru):
        self.__umur = umur_baru

    @property
    def keluhan(self):
        return self.__keluhan

    @keluhan.setter
    def keluhan(self, keluhan_baru):
        self.__keluhan = keluhan_baru

    @property
    def ruangan(self):
        return self.__ruangan

    @ruangan.setter
    def ruangan(self, ruangan_baru):
        self.__ruangan = ruangan_baru

    def tampilkan_info(self):
        print(f"Nama: {self.nama}, Umur: {self.umur}, Keluhan: {self.keluhan}, Ruangan: {self.ruangan}")

class Klinik:
    def __init__(self):
        self.daftar_pasien = []

    def cari_pasien(self, nama):
        for pasien in self.daftar_pasien:
            if pasien.nama.lower() == nama.lower():
                return pasien
        return None

    def tambah_pasien(self, pasien):
        if self.cari_pasien(pasien.nama):
            print("Pasien dengan nama tersebut sudah terdaftar.")
        else:
            self.daftar_pasien.append(pasien)
            print(f"Pasien '{pasien.nama}' berhasil ditambahkan.")

    def tampilkan_semua_pasien(self):
        if not self.daftar_pasien:
            print("Belum ada pasien terdaftar.")
        else:
            print("\nDaftar Pasien:")
            for pasien in self.daftar_pasien:
                pasien.tampilkan_info()

    def edit_data_pasien(self, nama):
        pasien = self.cari_pasien(nama)
        if pasien:
            print("Biarkan kosong jika tidak ingin mengubah.")
            nama_baru = input("Nama baru: ").strip()
            umur_baru = input("Umur baru: ").strip()
            keluhan_baru = input("Keluhan baru: ").strip()

            if nama_baru:
                pasien.nama = nama_baru
            if umur_baru.isdigit():
                pasien.umur = int(umur_baru)
            elif umur_baru:
                print("Umur harus berupa angka. Data umur tidak diubah.")
            if keluhan_baru:
                pasien.keluhan = keluhan_baru

            print("Data pasien berhasil diperbarui.")
        else:
            print("Pasien tidak ditemukan.")

    def edit_ruangan_pasien(self, nama):
        pasien = self.cari_pasien(nama)
        if pasien:
            ruangan_baru = input(f"Masukkan ruangan baru untuk {pasien.nama}: ").strip()
            if ruangan_baru:
                pasien.ruangan = ruangan_baru
                print("Ruangan pasien berhasil diperbarui.")
            else:
                print("Input ruangan kosong. Tidak diubah.")
        else:
            print("Pasien tidak ditemukan.")

    def hapus_pasien(self, nama):
        pasien = self.cari_pasien(nama)
        if pasien:
            self.daftar_pasien.remove(pasien)
            print(f"Pasien '{nama}' berhasil dihapus.")
        else:
            print("Pasien tidak ditemukan.")

    # === FITUR BARU: Cari pasien berdasarkan ruangan ===
    def cari_pasien_berdasarkan_ruangan(self, ruangan):
        ditemukan = False
        print(f"\nPasien di ruangan '{ruangan}':")
        for pasien in self.daftar_pasien:
            if pasien.ruangan.lower() == ruangan.lower():
                pasien.tampilkan_info()
                ditemukan = True
        if not ditemukan:
            print("Tidak ada pasien di ruangan tersebut.")

def menu_klinik():
    klinik = Klinik()

    while True:
        print("\n=== MENU KLINIK ===")
        print("1. Tambah Pasien")
        print("2. Tampilkan Semua Pasien")
        print("3. Edit Data Pasien")
        print("4. Edit Ruangan Pasien")
        print("5. Hapus Pasien")
        print("6. Cari Pasien Berdasarkan Ruangan")
        print("7. Keluar")

        pilihan = input("Pilih menu (1-7): ")

        if pilihan == "1":
            nama = input("Masukkan nama pasien: ").strip()
            umur = input("Masukkan umur pasien: ").strip()
            keluhan = input("Masukkan keluhan pasien: ").strip()
            ruangan = input("Masukkan ruangan pasien: ").strip()

            if umur.isdigit():
                pasien = Pasien(nama, int(umur), keluhan, ruangan)
                klinik.tambah_pasien(pasien)
            else:
                print("Umur harus berupa angka!")

        elif pilihan == "2":
            klinik.tampilkan_semua_pasien()

        elif pilihan == "3":
            nama = input("Masukkan nama pasien yang ingin diedit: ").strip()
            klinik.edit_data_pasien(nama)

        elif pilihan == "4":
            nama = input("Masukkan nama pasien yang ingin diubah ruangannya: ").strip()
            klinik.edit_ruangan_pasien(nama)

        elif pilihan == "5":
            nama = input("Masukkan nama pasien yang ingin dihapus: ").strip()
            klinik.hapus_pasien(nama)

        elif pilihan == "6":
            ruangan = input("Masukkan nama ruangan yang ingin dicari: ").strip()
            klinik.cari_pasien_berdasarkan_ruangan(ruangan)

        elif pilihan == "7":
            print("Terima kasih telah menggunakan sistem klinik.")
            break

        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    menu_klinik()
