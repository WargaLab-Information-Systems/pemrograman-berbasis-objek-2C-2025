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

    @property
    def jumlah_halaman(self):
        return self.__jumlah_halaman

class Perpustakaan:
    daftar_buku = []
    def cari_buku(self, judul):
        for buku in self.daftar_buku:
            if buku.judul == judul:
                return buku
        return None
    
    def tambah_buku(self):
        print("\n --- Masukkan data buku ---")
        judul = input("Judul          : ")
        penulis = input("Penulis        : ")
        jumlah_halaman = input("Jumlah Halaman : ")

        if jumlah_halaman.isdigit():
            buku = Buku(judul, penulis, jumlah_halaman)
            self.daftar_buku.append(buku)
            print("\n --- Buku berhasil ditambahkan --- ")
        else:
            print("\n --- Jumlah halaman harus berupa angka positif --- ")

    def tampilkan_buku(self):
        if len(self.daftar_buku) == 0:
            print("\n --- Belum ada buku di perpustakaan ---")
        else:
            print("\n --- Daftar Buku di Perpustakaan UTM --- ")
            index = 1
            for buku in self.daftar_buku:
                print(f"-- Data buku ke-{index} --")
                print("Judul   : ", buku.judul)
                print("Penulis : ", buku.penulis)
                print("Halaman : ", buku.jumlah_halaman)
                print("-" * 30)
                index += 1

    def edit(self):
        print("\n--- EDIT DATA BUKU ---")
        if len(self.daftar_buku) == 0:
            print("\n --- Belum ada data buku --- ")
            return

        judul = input("Masukkan judul buku yang ingin diubah: ")
        buku = self.cari_buku(judul)

        if buku:
            print(f"\n --- Data lama ---")
            print(f"Judul: {buku.judul}")
            print(f"Penulis: {buku.penulis}")
            print(f"Halaman: {buku.jumlah_halaman}")
            print("-" * 30)
            penulis_baru = input("Penulis Baru       : ")
            halaman_baru = input("Jumlah Halaman Baru: ")

            if halaman_baru.isdigit():
                buku._Buku__penulis = penulis_baru
                buku._Buku__jumlah_halaman = halaman_baru
                print("\n --- Data buku berhasil diubah --- ")
            else:
                print("\n --- Jumlah halaman harus angka --- ")
        else:
            print("\n --- Buku tidak ditemukan --- ")

    def delete(self):
        print("\n--- HAPUS DATA BUKU ---")
        if len(self.daftar_buku) == 0:
            print("\n --- Belum ada data buku --- ")
            return

        judul = input("Masukkan judul buku yang ingin dihapus: ")
        for i in range(len(self.daftar_buku)):
            if self.daftar_buku[i].judul == judul:
                del self.daftar_buku[i]
                print(f"\n --- Buku '{judul}' berhasil dihapus --- ")
                return

        print(f"\n --- Buku '{judul}' tidak ditemukan --- ")

def main():
    perpustakaan = Perpustakaan()

    while True:
        print("\n === SELAMAT DATANG DI PERPUS UTM ===")
        print("1. Tambah Buku")
        print("2. Tampilkan Buku")
        print("3. Edit Buku")
        print("4. Hapus Buku")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            perpustakaan.tambah_buku()
        elif pilihan == "2":
            perpustakaan.tampilkan_buku()
        elif pilihan == "3":
            perpustakaan.edit()
        elif pilihan == "4":
            perpustakaan.delete()
        elif pilihan == "5":
            print("\n === Terima kasih ===")
            print("    === Perpus UTM ===")
            break
        else:
            print("\n -- Pilihan tidak valid. Silakan coba lagi --")


main()