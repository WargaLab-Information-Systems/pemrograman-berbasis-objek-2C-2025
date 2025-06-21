class Buku:
    def __init__(self,judul,penulis,jumlah_halaman):
        self.__judul = judul
        self.__penulis = penulis
        self.__jumlah_halaman=jumlah_halaman
    
    def get_info(self):
        return f"Judul : {self.__judul},Penulis :{self.__penulis},jumlah halaman:{self.__jumlah_halaman}"
    
class Perpustakaan:
    def __init__(self):
        self.daftar_buku =[]

    def tambah_buku(self,judul,penulis,jumlah_halaman):
        buku_baru =Buku(judul,penulis,jumlah_halaman)
        self.daftar_buku.append(buku_baru)
        print(f"Buku '{judul}' berhasil ditambahkan.")

    def tampilkan_buku(self):
        if not self.daftar_buku:
            print("Belum ada buku di perpustakaan.")
        else:
            print("Daftar Buku di Perpustakaan:")
            for index, buku in enumerate(self.daftar_buku, start=1):
                print(f"{index}. {buku.get_info()}")
def main():
    perpustakaan = Perpustakaan()
    perpustakaan.tambah_buku("Laskar Pelangi", "Andrea Hirata", 529)
    perpustakaan.tambah_buku("Angkasa", "Ravinkyu", 336)
    perpustakaan.tambah_buku("Dikta & Hukum", "Dhia'an Farah", 388)
    print()
    perpustakaan.tampilkan_buku()
if __name__ == "__main__":
    main()  