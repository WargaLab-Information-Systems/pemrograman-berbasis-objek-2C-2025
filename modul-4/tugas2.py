class Buku:
    def __init__(self, judul, penulis, jumlah_halaman):
        self.__judul = judul
        self.__penulis = penulis
        self.__jumlah_halaman = jumlah_halaman

    def get_judul(self):
        return self.__judul
    
    def get_penulis(self):
        return self.__penulis
    
    def get_jumlah_halaman(self):
        return self.__jumlah_halaman

    def __str__(self):
        return f"Judul: {self.__judul}, Penulis: {self.__penulis}, Jumlah Halaman: {self.__jumlah_halaman}"


class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)
        print(f"Buku '{buku.get_judul()}' berhasil ditambahkan.")

    def tampilkan_semua_buku(self):
        if not self.daftar_buku:
            print("Belum ada buku di perpustakaan.")
        else:
            print("\n=== Daftar Buku di Perpustakaan ===")
            for i, buku in enumerate(self.daftar_buku, start=1):
                print(f"{i}. {buku}")


def jalankan_program():
    perpustakaan = Perpustakaan()

    while True:
        print("\n===== MENU PERPUSTAKAAN =====")
        print("1. Tambah Buku")
        print("2. Tampilkan Semua Buku")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == "1":
            judul = input("Masukkan judul buku: ")
            penulis = input("Masukkan nama penulis: ")
            jumlah_halaman_input = input("Masukkan jumlah halaman: ")

            if jumlah_halaman_input.isdigit():
                jumlah_halaman = int(jumlah_halaman_input)
                buku = Buku(judul, penulis, jumlah_halaman)
                perpustakaan.tambah_buku(buku)
            else:
                print("Input jumlah halaman harus berupa angka. Data buku tidak ditambahkan.")

        elif pilihan == "2":
            perpustakaan.tampilkan_semua_buku()

        elif pilihan == "3":
            print("Program selesai. Terima kasih.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")


if __name__ == "__main__":
    jalankan_program()
