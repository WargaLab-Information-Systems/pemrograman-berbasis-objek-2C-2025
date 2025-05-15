class Pasien:
    def __init__(self, nama, umur, keluhan):
        self.__nama = nama
        self.__umur = umur
        self.__keluhan = keluhan

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def umur(self):
        return self.__umur

    @umur.setter
    def umur(self, value):
        if value >= 0:
            self.__umur = value

    @property
    def keluhan(self):
        return self.__keluhan

    @keluhan.setter
    def keluhan(self, value):
        self.__keluhan = value


class Klinik:
    def __init__(self):
        self.__daftar_pasien = []

    def tambah_pasien(self, nama, umur, keluhan):
        pasien_baru = Pasien(nama, umur, keluhan)
        self.__daftar_pasien.append(pasien_baru)

    def tampilkan_pasien(self):
        if not self.__daftar_pasien:
            print("Belum ada data pasien.")
        else:
            print("=== Daftar Pasien Klinik ===")
            for idx, pasien in enumerate(self.__daftar_pasien, start=1):
                print(f"{idx}. Nama: {pasien.nama}, Umur: {pasien.umur}, Keluhan: {pasien.keluhan}")


def main():
    klinik = Klinik()

    klinik.tambah_pasien("Rina", 25, "Demam")
    klinik.tambah_pasien("Budi", 32, "Batuk")
    klinik.tambah_pasien("Sari", 45, "Sakit kepala")

    klinik.tampilkan_pasien()


if __name__ == "__main__":
    main()
