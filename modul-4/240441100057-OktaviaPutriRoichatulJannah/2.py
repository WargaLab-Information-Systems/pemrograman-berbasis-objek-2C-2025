class Buku:
    def __init__(self,judul,penulis,jmlh_hlm):
        self.__judul = judul
        self.__penulis = penulis
        self.__jmlh_hlm = jmlh_hlm

    @property
    def judul(self):
        return self.__judul
    
    @judul.setter
    def judul(self,jdl_baru):
        if len(jdl_baru) <= 50:
            self.__judul = jdl_baru
        else:
            print(f"Nama {jdl_baru} tidak valid!!")
    
    @property
    def penulis(self):
        return self.__penulis
    
    @penulis.setter
    def penulis(self, penulis_baru):
        nama_nospasi = penulis_baru.replace(" ", "")
        if nama_nospasi.isalpha():
            self.__penulis = penulis_baru
        else:
            print(f"Nama penulis '{penulis_baru}' tidak valid!!")
    
    @property
    def jml_hlm(self):
        return self.__jmlh_hlm
    
    @jml_hlm.setter
    def jml_hlm(self,hlm_baru):
        if  1 <= hlm_baru <= 5000:
            self.__jmlh_hlm = hlm_baru
        else:
            print(f"Jumlah halaman sebanyak {hlm_baru} tidak valid !!")

    def display(self):
        print(f"Judul           : {self.__judul}")
        print(f"Penulis         : {self.__penulis}")
        print(f"Jumlah Halaman  : {self.__jmlh_hlm} halaman")
        print()

class Perpustakaan:
    list_buku = []

    @classmethod
    def tambah_buku(cls, buku):
        cls.list_buku.append(buku)
        print(f"Buku dengan judul '{buku.judul}' berhasil ditambahkan")

    @classmethod
    def tampilkan_semua_buku(cls):
        print()
        print("=" * 45)
        print(f"{" " * 13}Data Manajemen Buku")
        print("=" * 45)
        print()
        nomor = 1
        for i in cls.list_buku:
            print(f"Data Buku ke-{nomor}")
            i.display()
            nomor += 1


class Main:
    def run():
        bku1 = Buku("Hello","Tere Liye",320)
        bku2 = Buku("Dunia Sophie(Sophie's World)","Jostein Gaarder",518)
        bku3 = Buku("Negeri Para Bedebah","Tere Liye",440)
        bku4 = Buku("Laut Bercerita","Leila S. Chudori",379)
        bku5 = Buku("Pulang","Tere Liye",400)
        bku6 = Buku("Pergi","Tere Liye",440)

        Perpustakaan.tambah_buku(bku1)
        Perpustakaan.tambah_buku(bku2)
        Perpustakaan.tambah_buku(bku3)
        Perpustakaan.tambah_buku(bku4)
        Perpustakaan.tambah_buku(bku5)
        Perpustakaan.tambah_buku(bku6)
        print()

        bku1.judul = "Hujan"
        bku2.penulis = "Jos4tein G44rder"
        bku3.jml_hlm = 7459

        Perpustakaan.tampilkan_semua_buku()

Main.run()