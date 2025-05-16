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

    def tambah_pasien(self, pasien):
        self.__daftar_pasien.append(pasien)

    def tampilkan_pasien(self):
        if not self.__daftar_pasien:
            print("Belum ada pasien yang terdaftar.")
        else:
            print("Daftar Pasien di Klinik:\n")
            for i, pasien in enumerate(self.__daftar_pasien, start=1):
                print(f"Pasien {i}:")
                print(f"  Nama    : {pasien.nama}")
                print(f"  Umur    : {pasien.umur}")
                print(f"  Keluhan : {pasien.keluhan}")
                print()

class    main():
    klinik = Klinik()

    pasien1 = Pasien("Andi", 30, "Demam")
    pasien2 = Pasien("Siti", 24, "Batuk")

    pasien2.keluhan = "Batuk dan Pilek"
    pasien1.umur = 31  

    klinik.tambah_pasien(pasien1)
    klinik.tambah_pasien(pasien2)

    klinik.tampilkan_pasien()





