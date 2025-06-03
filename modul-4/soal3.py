class Pasien:
    def __init__(self, nama, umur, keluhan):
        self.__nama = nama
        self.__umur = umur
        self.__keluhan = keluhan

    def get_info(self):
        return f"Nama: {self.__nama}, Umur: {self.__umur}, Keluhan: {self.__keluhan}"


class Klinik:
    def __init__(self):
        self.pasien_list = []

    def tambah_pasien(self, pasien):
        self.pasien_list.append(pasien)

    def tampilkan_pasien(self):
        print("DAFTAR NAMA PASIEN")
        for p in self.pasien_list:
            print(p.get_info())


klinik = Klinik()

p1 = Pasien("Sri", 19, "Demam")
p2 = Pasien("Oliver", 21, "Sakit kepala")

klinik.tambah_pasien(p1)
klinik.tambah_pasien(p2)

klinik.tampilkan_pasien()
