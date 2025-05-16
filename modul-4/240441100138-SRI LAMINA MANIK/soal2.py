class Buku:
    def __init__(self, judul, penulis, halaman):
        self.__judul = judul
        self.__penulis = penulis
        self.__halaman = halaman

    def get_info(self):
        return f"Judul: {self.__judul}, Penulis: {self.__penulis}, Halaman: {self.__halaman}"

    def get_judul(self):
        return self.__judul

    def set_judul(self, judul_baru):
        self.__judul = judul_baru

    def get_penulis(self):
        return self.__penulis

    def set_penulis(self, penulis_baru):
        self.__penulis = penulis_baru

    def get_halaman(self):
        return self.__halaman

    def set_halaman(self, halaman_baru):
        self.__halaman = halaman_baru


class Perpustakaan:
    def __init__(self):
        self.buku_list = []

    def tambah_buku(self, buku):
        self.buku_list.append(buku)
        print(" Buku berhasil ditambahkan.")

    def tampilkan_buku(self):
        if len(self.buku_list) == 0:
            print(" Belum ada buku di perpustakaan.")
        else:
            print("\n DAFTAR BUKU:")
            for i, b in enumerate(self.buku_list):
                print(f"{i+1}. {b.get_info()}")

    def cari_buku(self, kata_kunci):
        hasil = []
        for b in self.buku_list:
            if kata_kunci.lower() in b.get_judul().lower() or kata_kunci.lower() in b.get_penulis().lower():
                hasil.append(b)
        return hasil

    def edit_buku(self, index):
        if 0 <= index < len(self.buku_list):
            buku = self.buku_list[index]
            print(" Buku ditemukan:")
            print(buku.get_info())

            judul_baru = input("Masukkan judul baru (kosongkan jika tidak ingin mengubah): ")
            if judul_baru.strip():
                buku.set_judul(judul_baru)

            penulis_baru = input("Masukkan penulis baru (kosongkan jika tidak ingin mengubah): ")
            if penulis_baru.strip():
                buku.set_penulis(penulis_baru)

            halaman_baru = input("Masukkan jumlah halaman baru (kosongkan jika tidak ingin mengubah): ")
            if halaman_baru.strip():
                try:
                    buku.set_halaman(int(halaman_baru))
                except ValueError:
                    print(" Jumlah halaman harus berupa angka.")
            print(" Buku berhasil diperbarui.")
        else:
            print(" Nomor buku tidak ditemukan.")

    def hapus_buku(self, index):
        if 0 <= index < len(self.buku_list):
            buku = self.buku_list.pop(index)
            print(f" Buku '{buku.get_judul()}' sudah dihapus.")
        else:
            print(" Nomor buku tidak valid.")


# ===== PROGRAM UTAMA =====

perpus = Perpustakaan()

while True:
    print("\n MENU PERPUSTAKAAN")
    print("1. Tambah Buku")
    print("2. Cari Buku")
    print("3. Edit Buku")
    print("4. Hapus Buku")
    print("5. Tampilkan Semua Buku")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        judul = input("Masukkan judul buku: ")
        penulis = input("Masukkan penulis buku: ")
        try:
            halaman = int(input("Masukkan jumlah halaman: "))
            buku_baru = Buku(judul, penulis, halaman)
            perpus.tambah_buku(buku_baru)
        except ValueError:
            print(" Jumlah halaman harus angka. Buku gagal ditambahkan.")

    elif pilihan == "2":
        keyword = input("Masukkan kata kunci judul/penulis: ")
        hasil = perpus.cari_buku(keyword)
        if hasil:
            print(f"\n Ditemukan {len(hasil)} buku:")
            for b in hasil:
                print(b.get_info())
        else:
            print(" Buku tidak ditemukan.")

    elif pilihan == "3":
        perpus.tampilkan_buku()
        try:
            idx = int(input("Masukkan nomor buku yang mau diedit: ")) - 1
            perpus.edit_buku(idx)
        except ValueError:
            print(" Input harus angka.")

    elif pilihan == "4":
        perpus.tampilkan_buku()
        try:
            idx = int(input("Masukkan nomor buku yang mau dihapus: ")) - 1
            perpus.hapus_buku(idx)
        except ValueError:
            print(" Input harus angka.")

    elif pilihan == "5":
        perpus.tampilkan_buku()

    elif pilihan == "6":
        print(" Terima kasih telah menggunakan program perpustakaan!")
        break

    else:
        print(" Pilihan tidak valid, coba lagi.")
