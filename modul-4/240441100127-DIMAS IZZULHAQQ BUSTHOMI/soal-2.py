class Perpustakaan:
    def __init__(self):
        self.list_buku = []

    def tambahkan_buku(self, buku):
        self.list_buku.append(buku)
        print("-----" * 8)
        print(f"Buku dengan judul {buku.get_judul} berhasil dicatat.")
        print("-----" * 8)
    
    def tampilkan_buku(self):
        for buku in self.list_buku:
            buku.info()

    def delete(self, hapus):
        for buku in self.list_buku:
            if buku.get_judul == hapus:
                self.list_buku.remove(buku)
                print(f"Berhasil menghapus buku dengan judul {hapus}.")

class Buku:
    def __init__(self, judul, penulis, jumlah_halaman):
        self.__judul = judul
        self.__penulis = penulis
        self.__jumlah_halaman = jumlah_halaman

    @property
    def get_judul(self):
        return self.__judul
    
    @property
    def get_penulis(self):
        return self.__penulis
    
    @property
    def get_jumlah_halaman(self):
        return self.__jumlah_halaman
    
    @get_judul.setter
    def set_judul(self, judul_baru):
        self.__judul = judul_baru
    
    @get_penulis.setter
    def set_penulis(self, penulis_baru):
        self.__penulis = penulis_baru
    
    @get_jumlah_halaman.setter
    def set_jumlah_halaman(self, halaman_baru):
        self.__jumlah_halaman = halaman_baru

    def info(self):
        print("-----" * 8)
        print(f"Judul Buku     : {self.get_judul}")
        print(f"Penulis Buku   : {self.get_penulis}")
        print(f"Jumlah Halaman : {self.get_jumlah_halaman}")

class Main:
    perpus = Perpustakaan()

    while True:
        print("=== SELAMAT DATANG DI PERPUSTAKAAN ===")
        print("1. Catat Buku")
        print("2. Ubah Detail Buku")
        print("3. Tampilkan Semua Buku")
        print("4. Hapus")
        print("5. Keluar")
        print("-----" * 8)
        menu = input("Pilih Menu : ")
        print("-----" * 8)

        if menu == "1":
            print("Masukkan Data Buku ---")
            judul = input("Masukkan Judul : ")
            penulis = input("Masukkan Penulis : ")
            halaman = input("Masukkan Jumlah Halaman : ")
            
            buku = Buku(judul, penulis, halaman)
            perpus.tambahkan_buku(buku)

        elif menu == "2":
            cari = input("Masukkan Nama Buku : ")
            print("-----" * 8)
            pencarian = False

            for buku in perpus.list_buku:
                if buku.get_judul == cari:
                    judul_baru = input("Masukkan Judul Baru : ")
                    penulis_baru = input("Masukkan Penulis Baru : ")
                    jumlah_halaman_baru = input("Masukkan Jumlah Halaman Baru : ")
                    print("-----" * 8)

                    buku.set_judul = judul_baru
                    buku.set_penulis = penulis_baru
                    buku.set_jumlah_halaman = jumlah_halaman_baru

                    pencarian = True
                    break
                
            if not pencarian:
                print("Buku tidak ada.")
                print("-----" * 8)

        elif menu == "3":
            perpus.tampilkan_buku()
            print("-----" * 8)

        elif menu == "4":
            print("----- Hapus Buku -----")
            perpus.tampilkan_buku()
            hapus = input("Pilih yang dihapus :")
            perpus.delete(hapus)

        elif menu == "5":
            print("Terimakasih.")
            print("-----" * 8)
            break