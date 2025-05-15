class Pasien:
    def __init__(self,nama,umur,keluhan):
        self.__nama = nama
        self.__umur = umur
        self.__keluhan = keluhan

    @property
    def nama(self):
        return self.__nama
    
    @nama.setter
    def nama(self, nama_baru):
        nama_nospasi = nama_baru.replace(" ","")
        if nama_nospasi.isalpha():
            self.__nama = nama_baru
        else:
            print(f"Nama pasien '{nama_baru}' tidak valid!!")
    
    @property
    def umur(self):
        return self.__umur
    
    @umur.setter
    def umur(self,umur_baru):
        try:
            umur_baru = int(umur_baru)
            if 0 < umur_baru < 130:
                self.__umur = umur_baru
            else:
                print(f"Umur {umur_baru} tidak masuk akal!!")
        except ValueError:
            print(f"Umur '{umur_baru}' pasien tidak valid!!")
    
    @property
    def keluhan(self):
        return self.__keluhan
    
    @keluhan.setter
    def keluhan(self,keluhan_baru):
        if keluhan_baru.strip():
            self.__keluhan = keluhan_baru
        else:
            print("Keluhan pasien tidak boleh kosong!!")
    
    def display(self):
        print(f"Nama       : {self.__nama}")
        print(f"Umur       : {self.__umur} tahun")
        print(f"Keluhan    : {self.__keluhan}")
        print()


class Klinik:
    list_pasien = []
    
    @classmethod
    def tambah_pasien(cls, pasien):
        cls.list_pasien.append(pasien)
        print(f"Data pasien '{pasien.nama}' berhasil ditambahkan")

    @classmethod
    def tampilkan_semua_pasien(cls):
        print()
        print("=" * 35)
        print(f"{" " * 12}Data Pasien")
        print("=" * 35)
        print()
        nomor = 1
        for i in cls.list_pasien:
            print(f"Pasien ke-{nomor}")
            i.display()
            nomor += 1

    
class Main:
    def run():
        hmn1 = Pasien("SpongeBob SquarePants",21,"Happier Syndrom")
        hmn2 = Pasien("Patrick",22,"Lemotnesia")
        hmn3 = Pasien("Squidward Tentacles",34,"Iritasi Sosial")
        hmn4 = Pasien("Mr. Krab (Eugene Krabs)",63,"Hoarding Disorder")
        hmn5 = Pasien("Plankton (Sheldon J. Plankton)",37,"Krabbyphrenia Kronis")
        hmn6 = Pasien("Sandy Cheeks",26,"Hipersains Eksperimen")

        Klinik.tambah_pasien(hmn1)
        Klinik.tambah_pasien(hmn2)
        Klinik.tambah_pasien(hmn3)
        Klinik.tambah_pasien(hmn4)
        Klinik.tambah_pasien(hmn5)
        Klinik.tambah_pasien(hmn6)
        print()

        hmn1.nama = "Spong3bob Squ3rpent"
        hmn2.nama = "Patrick Star"
        hmn3.umur = "2A"
        hmn4.umur = 61
        hmn5.keluhan = " "

        Klinik.tampilkan_semua_pasien()

Main.run()