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


class Klinik:
    def __init__(self):
        self.daftar_pasien = []

    def tambah_pasien(self, nama, umur, keluhan):
        pasien_baru = Pasien(nama, umur, keluhan)
        self.daftar_pasien.append(pasien_baru)
        print(f"Pasien '{nama}' berhasil ditambahkan ke daftar.")

    def tampilkan_pasien(self):
        if not self.daftar_pasien:
            print("Belum ada pasien yang terdaftar.")
            return

        print("\nDaftar Pasien di Klinik:")
        for i, pasien in enumerate(self.daftar_pasien, 1):
            print(f"{i}. Nama: {pasien.get_nama()}, Umur: {pasien.get_umur()}, Keluhan: {pasien.get_keluhan()}")


def main():
    klinik = Klinik()

    klinik.tambah_pasien("Suryo Utomo", 24, "Demam dan sakit kepala")
    klinik.tambah_pasien("Tegar Firdaus", 32, "Batuk dan sesak napas")
    klinik.tambah_pasien("Diva Amalia", 45, "Tekanan darah tinggi")

    klinik.tampilkan_pasien()

if __name__ == "__main__":
    main()