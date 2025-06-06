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
        self._daftar_pasien = []

    def tambah_pasien(self, pasien):
        self._daftar_pasien.append(pasien)
        print(f"Pasien '{pasien.get_nama()}' berhasil ditambahkan.")

    def tampilkan_pasien(self):
        if not self._daftar_pasien:
            print("Belum ada pasien di klinik.")
            return

        print("\nDaftar Pasien di Klinik:")
        print("-" * 30)
        for idx, p in enumerate(self._daftar_pasien, start=1):
            print(f"{idx}. Nama    : {p.get_nama()}")
            print(f"   Umur    : {p.get_umur()} tahun")
            print(f"   Keluhan : {p.get_keluhan()}")
            print("-" * 30)

klinik = Klinik()

klinik.tambah_pasien(Pasien("Andi", 30, "Demam dan batuk"))
klinik.tambah_pasien(Pasien("Sari", 25, "Sakit kepala"))
klinik.tambah_pasien(Pasien("Budi", 40, "Nyeri punggung"))

klinik.tampilkan_pasien()