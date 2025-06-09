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

    def tambah_pasien(self, pasien):
        self.daftar_pasien.append(pasien)
        print(f"Pasien '{pasien.get_nama()}' berhasil ditambahkan.")

    def tampilkan_semua_pasien(self):
        print("\nDaftar Pasien di Klinik:")
        if not self.daftar_pasien:
            print("Belum ada pasien yang terdaftar.")
        else:
            for i, pasien in enumerate(self.daftar_pasien, start=1):
                print(f"{i}. Nama: {pasien.get_nama()}, Umur: {pasien.get_umur()}, Keluhan: {pasien.get_keluhan()}")

def main():
    klinik = Klinik()

    pasien1 = Pasien("Ayu", 25, "Demam")
    pasien2 = Pasien("Budi", 40, "Sakit Kepala")
    pasien3 = Pasien("Citra", 30, "Batuk Pilek")

    klinik.tambah_pasien(pasien1)
    klinik.tambah_pasien(pasien2)
    klinik.tambah_pasien(pasien3)

    klinik.tampilkan_semua_pasien()
    
main()
