class Klink:
    def __init__(self):
        self.list_pasien = []

    def tambah_pasien(self, pasien):
        self.list_pasien.append(pasien)
        print("-----" * 8)
        print(f"Pasien A.n {pasien.get_nama} berhasil ditambahkan.")

    def tampilkan_pasien(self):
        for pasien in self.list_pasien:
            pasien.info()

    def ubah(self, ubah):
        for pasien in self.list_pasien:
            if pasien.get_nama == ubah:
                print("Masukkan data baru")
                nama_baru = input("NAMA    : ")
                umur_baru = input("UMUR    : ")
                keluhan_baru = input("KELUHAN : ")
                pasien.set_nama = nama_baru
                pasien.set_umur =  umur_baru
                pasien.set_keluhan = keluhan_baru
                print("pasien berhasil diubah.")

class Pasien:
    def __init__(self, nama, umur, keluhan):
        self.__nama = nama
        self.__umur = umur
        self.__keluhan = keluhan

    @property
    def get_nama(self):
        return self.__nama
    
    @property
    def get_umur(self):
        return self.__umur
    
    @property
    def get_keluhan(self):
        return self.__keluhan
    
    @get_nama.setter
    def set_nama(self, ubah_nama):
        self.__nama = ubah_nama

    @get_umur.setter
    def set_umur(self, ubah_umur):
        self.__umur = ubah_umur
        
    @get_keluhan.setter
    def set_keluhan(self, ubah_keluhan):
        self.__keluhan = ubah_keluhan
        
    def info(self):
        print(f"Nama    : {self.get_nama}")
        print(f"Umur    : {self.get_umur}")
        print(f"Keluhan : {self.get_keluhan}")
        print("-----" * 8)
    
class main:
    klinik = Klink()

    while True:
        print("===== KLINIK INDOWO =====")
        print("1. Tambah Pasien")
        print("2. Tampilkan Semua Pasien")
        print("3. Ubah Pasien")
        print("4. Keluar")
        print("-----" * 8)
        menu = input("Pilih Menu : ")
        print("-----" * 8)
        
        if menu == "1":
            print("Masukkan Data Pasien")
            nama = input("Masukkan Nama    : ")
            umur = input("Masukkan Umur    : ")
            keluhan = input("Masukkan Keluhan : ")

            pasien = Pasien(nama, umur, keluhan)
            klinik.tambah_pasien(pasien)

        elif menu == "2":
            klinik.tampilkan_pasien()

        elif menu == "3":
            klinik.tampilkan_pasien()
            nama = input("Pilih yang ingin diuabah : ")
            klinik.ubah(nama)

        elif menu == "4":
            print("-----" * 8)
            print("TerimasKasih.")
            print("-----" * 8)
            break
