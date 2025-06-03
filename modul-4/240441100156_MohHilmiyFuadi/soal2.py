class Buku:
    def __init__(self, judul, penulis, jumlah_halaman):
        self.__judul = ""
        self.__penulis = ""
        self.__jumlah_halaman = 0

        self.set_judul(judul)
        self.set_penulis(penulis)
        self.set_jumlah_halaman(jumlah_halaman)

    def get_judul(self):
        return self.__judul

    def get_penulis(self):
        return self.__penulis

    def get_jumlah_halaman(self):
        return self.__jumlah_halaman

    def set_judul(self, judul):
        if judul != "":
            self.__judul = judul
        else:
            print("Judul tidak boleh kosong.")

    def set_penulis(self, penulis):
        if penulis != "":
            self.__penulis = penulis
        else:
            print("Penulis tidak boleh kosong.")

    def set_jumlah_halaman(self, jumlah_halaman):
        if jumlah_halaman > 0:
            self.__jumlah_halaman = jumlah_halaman
        else:
            print("Jumlah halaman harus lebih dari 0.")

    def data_valid(self):
        return self.__judul != "" and self.__penulis != "" and self.__jumlah_halaman > 0


class Perpustakaan:
    def __init__(self):
        self.__daftar_buku = []

    def tambah_buku(self, judul, penulis, jumlah_halaman):
        buku = Buku(judul, penulis, jumlah_halaman)
        if buku.data_valid():
            self.__daftar_buku.append(buku)
            print("Buku berhasil ditambahkan.")
        else:
            print("Gagal menambahkan buku karena data tidak valid.")

    def tampilkan_daftar_buku(self):
        if not self.__daftar_buku:
            print("Belum ada buku di perpustakaan.")
        else:
            print("\nDaftar Buku di Perpustakaan:")
            for i, buku in enumerate(self.__daftar_buku, start=1):
                print(f"{i}. {buku.get_judul()} | Penulis: {buku.get_penulis()} | Halaman: {buku.get_jumlah_halaman()}")

    def cari_buku(self, keyword):
        hasil = []
        for buku in self.__daftar_buku:
            if keyword.lower() in buku.get_judul().lower():
                hasil.append(buku)
        return hasil

    def ubah_buku(self, index, judul_baru, penulis_baru, halaman_baru):
        if 0 <= index < len(self.__daftar_buku):
            buku = self.__daftar_buku[index]
            buku.set_judul(judul_baru)
            buku.set_penulis(penulis_baru)
            buku.set_jumlah_halaman(halaman_baru)
            print("Data buku berhasil diubah.")
        else:
            print("Index buku tidak ditemukan.")

    def hapus_buku(self, index):
        if 0 <= index < len(self.__daftar_buku):
            del self.__daftar_buku[index]
            print("Buku berhasil dihapus.")
        else:
            print("Index buku tidak ditemukan.")


def main():
    perpustakaan = Perpustakaan()

    while True:
        print("\n=== Menu Perpustakaan ===")
        print("1. Tambah Buku")
        print("2. Tampilkan Daftar Buku")
        print("3. Cari Buku")
        print("4. Ubah Buku")
        print("5. Hapus Buku")
        print("6. Keluar")
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            judul = input("Masukkan judul buku: ")
            penulis = input("Masukkan nama penulis: ")
            halaman_input = input("Masukkan jumlah halaman: ")
            if halaman_input.isdigit():
                halaman = int(halaman_input)
                perpustakaan.tambah_buku(judul, penulis, halaman)
            else:
                print("Jumlah halaman harus berupa angka positif.")

        elif pilihan == "2":
            perpustakaan.tampilkan_daftar_buku()

        elif pilihan == "3":
            keyword = input("Masukkan judul buku yang dicari: ")
            hasil = perpustakaan.cari_buku(keyword)
            if hasil:
                print("\nHasil Pencarian:")
                for i, buku in enumerate(hasil, start=1):
                    print(f"{i}. {buku.get_judul()} | Penulis: {buku.get_penulis()} | Halaman: {buku.get_jumlah_halaman()}")
            else:
                print("Buku tidak ditemukan.")

        elif pilihan == "4":
            perpustakaan.tampilkan_daftar_buku()
            index = input("Masukkan nomor buku yang ingin diubah: ")
            if index.isdigit():
                idx = int(index) - 1
                judul = input("Judul baru: ")
                penulis = input("Penulis baru: ")
                halaman_input = input("Jumlah halaman baru: ")
                if halaman_input.isdigit():
                    halaman = int(halaman_input)
                    perpustakaan.ubah_buku(idx, judul, penulis, halaman)
                else:
                    print("Jumlah halaman harus angka.")
            else:
                print("Input tidak valid.")

        elif pilihan == "5":
            perpustakaan.tampilkan_daftar_buku()
            index = input("Masukkan nomor buku yang ingin dihapus: ")
            if index.isdigit():
                idx = int(index) - 1
                perpustakaan.hapus_buku(idx)
            else:
                print("Input tidak valid.")

        elif pilihan == "6":
            print("Terima kasih telah menggunakan program perpustakaan.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih antara 1 sampai 6.")


if __name__ == "__main__":
    main()
#  Ditambah cari buku sama kasi crud