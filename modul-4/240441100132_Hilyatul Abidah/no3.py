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
    def set_umur(self, umur_baru):
        self.__umur = umur_baru
    def set_keluhan(self, keluhan_baru):
        self.__keluhan = keluhan_baru
    def tampilkan_info(self):
        print(f"Nama     : {self.__nama}")
        print(f"Umur     : {self.__umur} tahun")
        print(f"Keluhan  : {self.__keluhan}")
        print("-" * 30)

class Klinik:
    def __init__(self):
        self.daftar_pasien = []
    def tambah_pasien(self, nama, umur, keluhan):
        pasien = Pasien(nama, umur, keluhan)
        self.daftar_pasien.append(pasien)
        print("✅ Pasien berhasil ditambahkan.")
    def tampilkan_semua_pasien(self):
        if not self.daftar_pasien:
            print("Belum ada pasien yang terdaftar.")
        else:
            print("\n=== DAFTAR PASIEN ===")
            for i, pasien in enumerate(self.daftar_pasien, start=1):
                print(f"Pasien ke-{i}")
                pasien.tampilkan_info()
    def cari_pasien_by_index(self, index):
        if 0 <= index < len(self.daftar_pasien):
            return self.daftar_pasien[index]
        return None
    def edit_pasien(self, index):
        pasien = self.cari_pasien_by_index(index)
        if pasien:
            print(f"✏️  Edit data untuk {pasien.get_nama()}")
            umur_baru = input("Umur baru: ")
            if umur_baru.isdigit():
                pasien.set_umur(int(umur_baru))
            keluhan_baru = input("Keluhan baru: ")
            if keluhan_baru.strip() != "":
                pasien.set_keluhan(keluhan_baru)
            print("✅ Data pasien berhasil diperbarui.")
        else:
            print("❌ Pasien tidak ditemukan.")
    def hapus_pasien(self, index):
        pasien = self.cari_pasien_by_index(index)
        if pasien:
            self.daftar_pasien.pop(index)
            print("🗑️ Pasien berhasil dihapus.")
        else:
            print("❌ Pasien tidak ditemukan.")

    def validasi_nama(self, teks):
        return teks.replace(" ", "").isalpha()

    def validasi_angka(self, teks):
        return teks.isdigit()

klinik = Klinik()
while True:
    print("\n=== MENU KLINIK ===")
    print("1. Tambah Pasien")
    print("2. Lihat Semua Pasien")
    print("3. Kelola Pasien (Edit / Hapus)")
    print("4. Keluar")
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        nama = input("Nama Pasien: ")
        while not klinik.validasi_nama(nama):
            print("❌ Nama hanya boleh huruf dan spasi.")
            nama = input("Masukkan Nama Pasien: ")
        umur = input("Umur Pasien: ")
        while not klinik.validasi_angka(umur):
            print("❌ Umur harus berupa angka.")
            umur = input("Masukkan Umur Pasien: ")
        keluhan = input("Keluhan Pasien: ")
        while not klinik.validasi_nama(keluhan):
            print("❌ Keluhan hanya boleh huruf dan spasi.")
            keluhan = input("Masukkan Keluhan Pasien: ")

        klinik.tambah_pasien(nama, int(umur), keluhan)

    elif pilihan == "2":
        klinik.tampilkan_semua_pasien()

    elif pilihan == "3":
        if not klinik.daftar_pasien:
            print("Belum ada pasien yang bisa diedit atau dihapus.")
        else:
            klinik.tampilkan_semua_pasien()
            index_input = input("Masukkan nomor pasien yang ingin diedit / dihapus: ")
            while not index_input.isdigit():
                print("❌ Harus berupa angka.")
                index_input = input("Masukkan nomor pasien yang ingin diedit / dihapus: ")
            index = int(index_input) - 1
            if klinik.cari_pasien_by_index(index) is None:
                print("❌ Nomor pasien tidak ditemukan.")
            else:
                print("1. Edit Pasien")
                print("2. Hapus Pasien")
                aksi = input("Pilih aksi (1/2): ")
                while aksi not in ["1", "2"]:
                    print("❌ Pilih 1 untuk Edit atau 2 untuk Hapus.")
                    aksi = input("Pilih aksi (1/2): ")
                if aksi == "1":
                    klinik.edit_pasien(index)
                else:
                    klinik.hapus_pasien(index)
    elif pilihan == "4":
        print("Terima kasih. Program selesai.")
        break
    else:
        print("❌ Pilihan tidak valid. Coba lagi.")

#menambahkan satu fitur lagi yang berisi edit/hapus, nama pasien gaperlu diedit, hanya umur dan keluhan dan delete pasien