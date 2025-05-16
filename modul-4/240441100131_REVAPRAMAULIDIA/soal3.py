#cari pasien edit dan hapus
class Pasien:
    def __init__(self, nama, umur, keluhan):
        self.__nama = nama
        self.__umur = umur
        self.__keluhan = keluhan

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama):
        self.__nama = nama

    def get_umur(self):
        return self.__umur

    def set_umur(self, umur):
        self.__umur = umur

    def get_keluhan(self):
        return self.__keluhan

    def set_keluhan(self, keluhan):
        self.__keluhan = keluhan

    def info_pasien(self):
        print(f"Nama Pasien: {self.get_nama()}")
        print(f"Umur: {self.get_umur()}")
        print(f"Keluhan: {self.get_keluhan()}")

class Klinik:
    def __init__(self):
        self.list_pasien = []

    def tambah_pasien(self, pasien):
        self.list_pasien.append(pasien)

    def info_klinik(self):
        if not self.list_pasien:
            print("Belum ada daftar pasien")
        else:
            for pasien in self.list_pasien:
                pasien.info_pasien()
                print("---")

    def cari_pasien(self, nama):
        return [(i, pasien) for i, pasien in enumerate(self.list_pasien) if pasien.get_nama().lower() == nama.lower()]

    def hapus_pasien(self, index):
        if 0 <= index < len(self.list_pasien):
            pasien = self.list_pasien.pop(index)
            print(f"Pasien '{pasien.get_nama()}' berhasil dihapus.")
        else:
            print("Index pasien tidak valid.")

    def edit_pasien(self, index, nama_baru, umur_baru, keluhan_baru):
        if 0 <= index < len(self.list_pasien):
            pasien = self.list_pasien[index]
            pasien.set_nama(nama_baru)
            pasien.set_umur(umur_baru)
            pasien.set_keluhan(keluhan_baru)
            print("Data pasien berhasil diperbarui.")
        else:
            print("Index pasien tidak valid.")


if __name__ == "__main__":
    klinik = Klinik()

    while True:
        print("\nMenu")
        print("1. Tambah Pasien")
        print("2. Info Pasien")
        print("3. Cari Pasien")
        print("4. Edit Pasien")
        print("5. Hapus Pasien")
        print("6. Keluar")

        pilihan = input("Pilihan (1/2/3/4/5/6): ")

        if pilihan == "1":
            while True:
                nama = input("Nama: ")

                while True:
                    umur_input = input("Umur: ")
                    if umur_input.isdigit():
                        umur = int(umur_input)
                        break
                    else:
                        print("Umur harus berupa angka! Silakan coba lagi.")

                keluhan = input("Keluhan: ")
                pasien = Pasien(nama, umur, keluhan)
                klinik.tambah_pasien(pasien)
                print("Data pasien berhasil ditambahkan.")

                lagi = input("Tambah pasien lagi? (y/n): ")
                if lagi.lower() != 'y':
                    break

        elif pilihan == "2":
            print("Info Pasien:")
            klinik.info_klinik()

        elif pilihan == "3":
            nama_cari = input("Masukkan nama pasien yang dicari: ")
            hasil = klinik.cari_pasien(nama_cari)
            if hasil:
                print(f"Ditemukan {len(hasil)} pasien dengan nama '{nama_cari}':")
                for i, (idx, pasien) in enumerate(hasil, 1):
                    print(f"{i}.")
                    pasien.info_pasien()
            else:
                print("Pasien tidak ditemukan.")

        elif pilihan == "4":
            nama_cari = input("Masukkan nama pasien yang ingin diedit: ")
            hasil = klinik.cari_pasien(nama_cari)
            if hasil:
                idx_pasien = hasil[0][0]
                pasien = hasil[0][1]

                print("Data pasien yang akan diedit:")
                pasien.info_pasien()
                print("---")

                nama_baru = input("Nama baru: ")
                while True:
                    umur_baru_input = input("Umur baru: ")
                    if umur_baru_input.isdigit():
                        umur_baru = int(umur_baru_input)
                        break
                    else:
                        print("Umur harus berupa angka!")
                keluhan_baru = input("Keluhan baru: ")
                klinik.edit_pasien(idx_pasien, nama_baru, umur_baru, keluhan_baru)
            else:
                print("Pasien tidak ditemukan.")


        elif pilihan == "5":
            nama_hapus = input("Masukkan nama pasien yang ingin dihapus: ")
            hasil = klinik.cari_pasien(nama_hapus)
            if hasil:
                idx_pasien = hasil[0][0]
                pasien = hasil[0][1]

                print("Data pasien yang akan dihapus:")
                pasien.info_pasien()
                konfirmasi = input("Yakin ingin menghapus pasien ini? (y/n): ").lower()
                if konfirmasi == 'y':
                    klinik.hapus_pasien(idx_pasien)
                    print("Pasien berhasil dihapus.")
                else:
                    print("Penghapusan dibatalkan.")
            else:
                print("Pasien tidak ditemukan.")

        elif pilihan == "6":
            print("Terima kasih telah menggunakan layanan klinik.")
            break

        else:
            print("Pilihan tidak valid, coba lagi.")