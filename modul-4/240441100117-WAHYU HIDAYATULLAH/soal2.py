class Buku:
    def __init__(self, judul, penulis, jumlah_hal):
        self.__judul = judul
        self.__penulis = penulis
        self.__jumlah_hal = jumlah_hal

    @property
    def judul(self):
        return self.__judul

    @judul.setter
    def judul(self, value):
        self.__judul = value

    @property
    def penulis(self):
        return self.__penulis

    @property
    def jumlah_hal(self):
        return self.__jumlah_hal

class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self, judul, penulis, jumlah_hal):
        buku_baru = Buku(judul, penulis, jumlah_hal)
        self.daftar_buku.append(buku_baru)
        print(f"Buku {judul} berhasil ditambahkan")

    def tampilkan_buku(self):
        print("\nDaftar Buku di Perpustakaan:")
        if not self.daftar_buku:
            print("Belum ada buku.")
        for i, buku in enumerate(self.daftar_buku, start=1):
            print(f"{i}. Judul          : {buku.judul}")
            print(f"   Penulis        : {buku.penulis}")
            print(f"   Jumlah Halaman : {buku.jumlah_hal}")
            print("-" * 40)

    def ubah_judul_buku(self, nomor, judul_baru):
        if 1 <= nomor <= len(self.daftar_buku):
            self.daftar_buku[nomor-1].judul = judul_baru
            print("Judul buku berhasil diubah.")
        else:
            print("Nomor buku tidak valid.")

    def hapus_buku(self, nomor):
        if 1 <= nomor <= len(self.daftar_buku):
            buku = self.daftar_buku.pop(nomor-1)
            print(f"Buku '{buku.judul}' berhasil dihapus.")
        else:
            print("Nomor buku tidak valid.")

class main:
    def __init__(self):
        self.perpustakaan = Perpustakaan()
        self.menu()

    def menu(self):
        while True:
            print("\n ====== Perpustakaan ======")
            print("1. Tambah Buku")
            print("2. Lihat Semua Buku")
            print("3. Ubah Judul Buku")
            print("4. Keluar")
            pilihan = input("Pilih Menu: ")

            if pilihan == "1":
                judul = input("Masukkan Judul Buku: ")
                penulis = input("Masukkan Penulis: ")
                hal = input("Masukkan Jumlah Halaman: ")
                self.perpustakaan.tambah_buku(judul, penulis, hal)
            elif pilihan == "2":
                self.perpustakaan.tampilkan_buku()
            elif pilihan == "3":
                self.perpustakaan.tampilkan_buku()
                nomor = input("Masukkan nomor buku yang ingin diubah: ")
                judul_baru = input("Masukkan judul baru: ")
                self.perpustakaan.ubah_judul_buku(int(nomor), judul_baru)
            elif pilihan == "4":
                print("Terima kasih!")
                break
            else:
                print("Pilihan harus sesuai")

main()