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
        self.__daftar_pasien = []

    def tambah_pasien(self, pasien):
        self.__daftar_pasien.append(pasien)
        print(f"Nona/Tuan {pasien.get_nama()} berhasil ditambahkan.")

    def tampilkan_pasien(self):
        if not self.__daftar_pasien:
            print("Belum ada pasien di klinik.")
            return
        print("Daftar Pasien di Klinik:")
        print("▪" * 35)
        for pasien in self.__daftar_pasien:
            print(f"Nama     : {pasien.get_nama()}")
            print(f"Umur     : {pasien.get_umur()} tahun")
            print(f"Keluhan  : {pasien.get_keluhan()}")
            print("▪" * 35)


def main():
    klinik = Klinik()

    klinik.tambah_pasien(Pasien("Kunikuzuzhi", 19, "Sakit Hati"))
    klinik.tambah_pasien(Pasien("Scaramouche", 18, "Sakit kepala"))
    klinik.tambah_pasien(Pasien("Wriothesley", 30, "Panas Tinggi"))

    print("❙" * 35)
    klinik.tampilkan_pasien()

if __name__ == "__main__":
    main()