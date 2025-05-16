class Buku:
    def __init__(self, judul, penulis, jumlah_halaman):
        self.__judul = judul
        self.__penulis = penulis
        self.__jumlah_halaman = jumlah_halaman

    @property
    def judul(self):
        return self.__judul

    @judul.setter
    def judul(self, judul_baru):
        self.__judul = judul_baru

    @property
    def penulis(self):
        return self.__penulis

    @penulis.setter
    def penulis(self, penulis_baru):
        self.__penulis = penulis_baru

    @property
    def jumlah_halaman(self):
        return self.__jumlah_halaman

    @jumlah_halaman.setter
    def jumlah_halaman(self, halaman_baru):
        self.__jumlah_halaman = halaman_baru

    def tampilkan_info(self):
        print(f"Judul: {self.judul}, Penulis: {self.penulis}, Halaman: {self.jumlah_halaman}")


class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []

    def cari_buku(self, judul):
        for buku in self.daftar_buku:
            if buku.judul.lower() == judul.lower():
                return buku
        return None

    def tambah_buku(self, buku):
        if self.cari_buku(buku.judul):
            print("Buku dengan judul tersebut sudah ada.")
        else:
            self.daftar_buku.append(buku)
            print(f"Buku '{buku.judul}' berhasil ditambahkan.")

    def tampilkan_semua_buku(self):
        if not self.daftar_buku:
            print("Belum ada buku di perpustakaan.")
        else:
            print("\nDaftar Buku:")
            for buku in self.daftar_buku:
                buku.tampilkan_info()

    def edit_buku(self, judul):
        buku = self.cari_buku(judul)
        if buku:
            print("Masukkan data baru (biarkan kosong jika tidak ingin mengubah):")
            judul_baru = input("Judul baru: ").strip()
            penulis_baru = input("Penulis baru: ").strip()
            halaman_baru = input("Jumlah halaman baru: ").strip()

            if judul_baru:
                buku.judul = judul_baru
            if penulis_baru:
                buku.penulis = penulis_baru
            if halaman_baru.isdigit():
                buku.jumlah_halaman = int(halaman_baru)
            elif halaman_baru:
                print("Jumlah halaman harus angka. Data halaman tidak diubah.")

            print("Data buku berhasil diperbarui.")
        else:
            print("Buku tidak ditemukan.")

    def pinjam_buku(self, judul):
        buku = self.cari_buku(judul)
        if buku:
            self.daftar_buku.remove(buku)
            print(f"Buku '{judul}' berhasil dipinjam.")
        else:
            print("Buku tidak ditemukan.")


def menu_perpustakaan():
    perpustakaan = Perpustakaan()

    while True:
        print("\n==== MENU PERPUSTAKAAN ====")
        print("1. Tambah Buku")
        print("2. Tampilkan Semua Buku")
        print("3. Edit Buku")
        print("4. Pinjam Buku")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            judul = input("Masukkan Judul Buku: ").strip()
            penulis = input("Masukkan Penulis: ").strip()
            halaman = input("Masukkan Jumlah Halaman: ").strip()
            if halaman.isdigit():
                buku = Buku(judul, penulis, int(halaman))
                perpustakaan.tambah_buku(buku)
            else:
                print("Jumlah halaman harus berupa angka!")

        elif pilihan == "2":
            perpustakaan.tampilkan_semua_buku()

        elif pilihan == "3":
            judul = input("Masukkan judul buku yang ingin diedit: ")
            perpustakaan.edit_buku(judul)

        elif pilihan == "4":
            judul = input("Masukkan judul buku yang ingin dipinjam: ")
            perpustakaan.pinjam_buku(judul)

        elif pilihan == "5":
            print("Terima kasih sudah menggunakan sistem perpustakaan.")
            break

        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    menu_perpustakaan()
