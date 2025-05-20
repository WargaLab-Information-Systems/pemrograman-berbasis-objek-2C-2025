class Buku:
    def __init__(self, judul, penulis, jumlah_halaman, stok):
        self.__judul = judul
        self.__penulis = penulis
        self.__jumlah_halaman = jumlah_halaman
        self.__stok = stok

    def get_judul(self):
        return self.__judul

    def get_penulis(self):
        return self.__penulis

    def get_jumlah_halaman(self):
        return self.__jumlah_halaman

    def get_stok(self):
        return self.__stok

    def set_stok(self, stok_baru):
        self.__stok = stok_baru

    def set_penulis(self, penulis_baru):
        self.__penulis = penulis_baru

    def set_jumlah_halaman(self, halaman_baru):
        self.__jumlah_halaman = halaman_baru

    def tampilkan_info(self):
        print(f"Judul          : {self.__judul}")
        print(f"Penulis        : {self.__penulis}")
        print(f"Jumlah Halaman : {self.__jumlah_halaman}")
        print(f"Stok           : {self.__stok}")
        print("-" * 30)

class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self, judul, penulis, jumlah_halaman, stok):
        buku = Buku(judul, penulis, jumlah_halaman, stok)
        self.daftar_buku.append(buku)
        print("Buku berhasil ditambahkan!")

    def tampilkan_semua_buku(self):
        if not self.daftar_buku:
            print("Belum ada buku dalam perpustakaan.")
        else:
            print("\n=== DAFTAR BUKU ===")
            for i, buku in enumerate(self.daftar_buku, start=1):
                print(f"Buku ke-{i}")
                buku.tampilkan_info()

    def cari_buku_berdasarkan_index(self, index):
        if 0 <= index < len(self.daftar_buku):
            return self.daftar_buku[index]
        return None

    def edit_buku(self, index):
        buku = self.cari_buku_berdasarkan_index(index)
        if buku:
            print("Masukkan data baru (tekan Enter jika tidak ingin mengubah):")
            penulis = input("Penulis baru: ")
            if penulis:
                buku.set_penulis(penulis)

            halaman = input("Jumlah Halaman baru: ")
            if halaman.isdigit():
                buku.set_jumlah_halaman(int(halaman))

            stok = input("Stok baru: ")
            if stok.isdigit():
                buku.set_stok(int(stok))

            print("Buku berhasil diperbarui.")
        else:
            print("Buku tidak ditemukan.")

    def hapus_buku(self, index):
        buku = self.cari_buku_berdasarkan_index(index)
        if buku:
            self.daftar_buku.pop(index)
            print("Buku berhasil dihapus.")
        else:
            print("❌ Buku tidak ditemukan.")

    def validasi_input_nama(self, input_string):
        return input_string.replace(" ", "").isalpha()

    def validasi_input_angka(self, input_string):
        return input_string.isdigit() and int(input_string) > 0


perpus = Perpustakaan()

while True:
    print("\n=== MENU PERPUSTAKAAN ===")
    print("1. Tambah Buku")
    print("2. Lihat Semua Buku")
    print("3. Kelola Buku (Edit / Hapus)")
    print("4. Keluar")
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        judul = input("Masukkan Judul Buku: ")
        penulis = input("Masukkan Nama Penulis: ")
        while not perpus.validasi_input_nama(penulis):
            print("Nama penulis hanya boleh huruf.")
            penulis = input("Masukkan Nama Penulis: ")

        halaman = input("Masukkan Jumlah Halaman: ")
        while not perpus.validasi_input_angka(halaman):
            print("Jumlah halaman harus berupa angka positif.")
            halaman = input("Masukkan Jumlah Halaman: ")

        stok = input("Masukkan Stok Buku: ")
        while not perpus.validasi_input_angka(stok):
            print("Stok harus berupa angka positif.")
            stok = input("Masukkan Stok Buku: ")

        perpus.tambah_buku(judul, penulis, int(halaman), int(stok))

    elif pilihan == "2":
        perpus.tampilkan_semua_buku()

    elif pilihan == "3":
        if not perpus.daftar_buku:
            print("Belum ada buku untuk dikelola.")
        else:
            perpus.tampilkan_semua_buku()
            try:
                index = int(input("Masukkan nomor buku yang ingin diedit / dihapus: ")) - 1
                if not (0 <= index < len(perpus.daftar_buku)):
                    print("Nomor buku tidak valid.")
                    continue

                print("1. Edit Buku")
                print("2. Hapus Buku")
                sub = input("Pilih aksi (1-2): ")

                if sub == "1":
                    perpus.edit_buku(index)
                elif sub == "2":
                    perpus.hapus_buku(index)
                else:
                    print("Pilihan tidak valid.")
            except ValueError:
                print("Input harus berupa angka.")

    elif pilihan == "4":
        print("Terima kasih telah menggunakan sistem perpustakaan.")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

# edit buku, delete, tambahkan fitur lagi nomor 3, menu nya berisi tentang judul buku,stock , judul boleh sama tapi stock beda