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
        if isinstance(value, int) and value > 0:
            self.__umur = value
        else:
            print("Umur tidak valid")

    @property
    def keluhan(self):
        return self.__keluhan

    @keluhan.setter
    def keluhan(self, value):
        self.__keluhan = value

    def info(self):
        print(f"Nama    : {self.__nama}")
        print(f"Umur    : {self.__umur}")
        print(f"Keluhan : {self.__keluhan}")
        print("-" * 30)

class Klinik:
    def __init__(self):
        self.__daftar_pasien = []

    def tambah_pasien(self, nama, umur, keluhan):
        pasien = Pasien(nama, umur, keluhan)
        self.__daftar_pasien.append(pasien)
        print(f"Pasien {nama} berhasil ditambahkan.")

    def tampilkan_pasien(self):
        if not self.__daftar_pasien:
            print("Tidak ada pasien di klinik.")
        for pasien in self.__daftar_pasien:
            pasien.info()

class Main:
    @staticmethod
    def run():
        klinik = Klinik()
        klinik.tambah_pasien("Andi", 25, "Demam")
        klinik.tambah_pasien("Siti", 30, "Sakit Kepala")
        print("\nDaftar Pasien:")
        klinik.tampilkan_pasien()

if __name__ == "__main__":
    Main.run()
