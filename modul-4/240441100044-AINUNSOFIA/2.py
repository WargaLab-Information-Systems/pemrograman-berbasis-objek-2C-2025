class Buku:
    def __init__(self, judul, penulis, halaman):
        self.__judul = judul
        self.__penulis = penulis
        self.__halaman = halaman

    # Getter dan Setter untuk Judul
    @property
    def judul(self):
        return self.__judul

    @judul.setter
    def judul(self, judul_baru):
        self.__judul = judul_baru

    # Getter dan Setter untuk Penulis
    @property
    def penulis(self):
        return self.__penulis

    @penulis.setter
    def penulis(self, penulis_baru):
        self.__penulis = penulis_baru

    # Getter dan Setter untuk Halaman
    @property
    def halaman(self):
        return self.__halaman

    @halaman.setter
    def halaman(self, jumlah_halaman):
        if jumlah_halaman > 0:
            self.__halaman = jumlah_halaman
        else:
            print("Jumlah halaman harus lebih dari 0")

    def tampilkan(self):
        print(f"Judul   : {self.__judul}")
        print(f"Penulis : {self.__penulis}")
        print(f"Halaman : {self.__halaman}")
        print("-" * 30)


class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)
        print("Buku berhasil ditambahkan.")

    def tampilkan_buku(self):
        if not self.daftar_buku:
            print("Belum ada buku dalam perpustakaan.")
        else:
            print("\nDaftar Buku di Perpustakaan:")
            for buku in self.daftar_buku:
                buku.tampilkan()


def main():
    perpustakaan = Perpustakaan()
    while True:
        print("\nMenu:")
        print("1. Tambah Buku")
        print("2. Lihat Semua Buku")
        print("3. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            judul = input("Masukkan Judul Buku: ")
            penulis = input("Masukkan Nama Penulis: ")
            try:
                halaman = int(input("Masukkan Jumlah Halaman: "))
                buku_baru = Buku(judul, penulis, halaman)
                perpustakaan.tambah_buku(buku_baru)
            except ValueError:
                print("Jumlah halaman harus angka!")

        elif pilihan == "2":
            perpustakaan.tampilkan_buku()

        elif pilihan == "3":
            print("Terima kasih telah menggunakan sistem perpustakaan.")
            break

        else:
            print("Pilihan tidak valid.")
            
main()