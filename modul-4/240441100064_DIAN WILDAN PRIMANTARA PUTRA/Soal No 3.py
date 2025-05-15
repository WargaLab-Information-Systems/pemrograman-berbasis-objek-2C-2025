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


class Klinik:
    def __init__(self):
        self.daftar_pasien = []

    def tambah_pasien(self, nama, umur, keluhan):
        pasien = Pasien(nama, umur, keluhan)
        self.daftar_pasien.append(pasien)

    def tampilkan_pasien(self):
        print("=== Daftar Pasien ===")
        for p in self.daftar_pasien:
            print(f"Nama: {p.nama}, Umur: {p.umur}, Keluhan: {p.keluhan}")

klinik = Klinik()
klinik.tambah_pasien("primantaraputra", 19, "Demam")
klinik.tambah_pasien("dynwlldn", 13, "sakit jiwa")
klinik.tampilkan_pasien()