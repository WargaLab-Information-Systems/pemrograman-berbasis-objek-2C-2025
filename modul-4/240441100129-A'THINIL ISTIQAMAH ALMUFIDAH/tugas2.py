class Buku:
    def __init__(self, judul, penulis, jumlah_halaman):
        self.__judul = judul
        self.__penulis = penulis
        self.__jumlah_halaman = jumlah_halaman

    @property
    def judul(self):
        return self.__judul

    @property
    def penulis(self):
        return self.__penulis

    @penulis.setter
    def penulis(self, value):
        self.__penulis = value

    @property
    def jumlah_halaman(self):
        return self.__jumlah_halaman

    @jumlah_halaman.setter
    def jumlah_halaman(self, value):
        self.__jumlah_halaman = value

    @property
    def info(self):
        return f"Judul: {self.__judul}, Penulis: {self.__penulis}, Halaman: {self.__jumlah_halaman}"


class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self, judul, penulis, jumlah_halaman):
        buku_baru = Buku(judul, penulis, jumlah_halaman)
        self.daftar_buku.append(buku_baru)
        print("Buku berhasil ditambahkan ke perpustakaan.")

    def tampilkan_semua_buku(self):
        if not self.daftar_buku:
            print("Belum ada buku di perpustakaan.")
        else:
            print("\nDaftar Buku di Perpustakaan:")
            for i, buku in enumerate(self.daftar_buku, 1):
                print(f"{i}. {buku.info}")

    def cari_buku(self, judul):
        return [(i, buku) for i, buku in enumerate(self.daftar_buku) if buku.judul.lower() == judul.lower()]


def main():
    perpustakaan = Perpustakaan()

    while True:
        print("\n--- MENU PERPUSTAKAAN ---")
        print("1. Tambah Buku")
        print("2. Tampilkan Semua Buku")
        print("3. Cari Buku")
        print("4. Edit Buku")
        print("5. Hapus Buku")
        print("6. Keluar")
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == '1':
            judul = input("Masukkan judul buku: ")
            penulis = input("Masukkan nama penulis: ")
            try:
                jumlah_halaman = int(input("Masukkan jumlah halaman: "))
                perpustakaan.tambah_buku(judul, penulis, jumlah_halaman)
            except ValueError:
                print("Jumlah halaman harus berupa angka.")

        elif pilihan == '2':
            perpustakaan.tampilkan_semua_buku()

        elif pilihan == '3':
            judul_cari = input("Masukkan judul buku yang dicari: ")
            hasil = perpustakaan.cari_buku(judul_cari)
            if hasil:
                print("Buku ditemukan:")
                for i, (idx, buku) in enumerate(hasil, 1):
                    print(f"{i}. {buku.info}")
            else:
                print("Buku tidak ditemukan.")

        elif pilihan == '4':
            judul_cari = input("Masukkan judul buku yang ingin diedit: ")
            hasil = perpustakaan.cari_buku(judul_cari)
            if hasil:
                idx_buku = hasil[0][0]
                buku = perpustakaan.daftar_buku[idx_buku]
                print(f"Mengedit buku: {buku.info}")

                buku.penulis = input("Penulis baru: ")
                while True:
                    jumlah_baru = input("Jumlah halaman baru: ")
                    if jumlah_baru.isdigit():
                        buku.jumlah_halaman = int(jumlah_baru)
                        break
                    else:
                        print("Masukkan angka yang valid.")
                print("Buku berhasil diedit.")
            else:
                print("Buku tidak ditemukan.")

        elif pilihan == '5':
            judul_hapus = input("Masukkan judul buku yang ingin dihapus: ")
            hasil = perpustakaan.cari_buku(judul_hapus)
            if hasil:
                idx_asli = hasil[0][0]
                hapus_buku = perpustakaan.daftar_buku.pop(idx_asli)
                print(f"Buku '{hapus_buku.judul}' telah dihapus.")
            else:
                print("Buku tidak ditemukan.")

        elif pilihan == '6':
            print("Terima kasih telah menggunakan sistem perpustakaan.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
#  edit delete cari