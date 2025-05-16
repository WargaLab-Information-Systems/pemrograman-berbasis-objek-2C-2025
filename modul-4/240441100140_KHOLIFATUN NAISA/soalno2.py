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
    @judul.setter
    def judul(self, judul):
        self.__judul = judul
    @penulis.setter
    def penulis(self, penulis):
        self.__penulis = penulis
    @jumlah_halaman.setter
    def jumlah_halaman(self, jumlah_halaman):
        self.__jumlah_halaman = jumlah_halaman

class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []
    def tambah_buku(self, judul, penulis, jumlah_halaman):
        buku_baru = Buku(judul, penulis, jumlah_halaman)
        self.daftar_buku.append(buku_baru)
    def tampilkan_semua_buku(self):
        if not self.daftar_buku:
            print("Tidak ada buku dalam daftar.")
        else:
            for i, buku in enumerate(self.daftar_buku, start=1):
                print(f"{i}. Judul: {buku.judul}, Penulis: {buku.penulis}, Jumlah Halaman: {buku.jumlah_halaman}")
    def edit(self):
        self.tampilkan_semua_buku()
        if not self.daftar_buku:
            return
        nomor = int(input("Masukkan nomor buku yang akan diubah: ")) - 1
        if 0 <= nomor < len(self.daftar_buku):
            buku = self.daftar_buku[nomor]
            nama_baru = input("Masukkan judul baru: ")
            penulis_baru = input("Masukkan penulis baru: ")
            jumlah_baru = int(input("Masukkan jumlah halaman baru: "))
            buku.judul = nama_baru
            buku.penulis = penulis_baru
            buku.jumlah_halaman = jumlah_baru
            print("Data berhasil diubah!")
        else:
            print("Data tidak ditemukan!")
    def hapus(self):
        self.tampilkan_semua_buku()
        if not self.daftar_buku:
            return
        nomor = int(input("Masukkan nomor buku yang akan dihapus: ")) - 1
        if 0 <= nomor < len(self.daftar_buku):
            self.daftar_buku.pop(nomor)
            print("Data berhasil dihapus!")
        else:
            print("Data tidak ditemukan!")
    def cari_buku(self):
        kata_kunci = input("Masukkan judul atau penulis yang dicari: ").lower()
        ditemukan = False
        for i, buku in enumerate(self.daftar_buku, start=1):
            if kata_kunci in buku.judul.lower() or kata_kunci in buku.penulis.lower():
                print(f"{i}. Judul: {buku.judul}, Penulis: {buku.penulis}, Jumlah Halaman: {buku.jumlah_halaman}")
                ditemukan = True
        if not ditemukan:
            print("Buku tidak ditemukan.")

def main():
    perpustakaan = Perpustakaan()
    while True:
        print("\nMenu Perpustakaan")
        print("1. Tambah Buku")
        print("2. Edit Buku")
        print("3. Cari Buku")
        print("4. Delete Buku")
        print("5. Tampilkan Buku")
        print("6. Keluar")
        pilihan = int(input("Pilih menu: "))
        if pilihan == 1:
            judul = input("Masukkan judul buku: ")
            penulis = input("Masukkan penulis buku: ")
            jumlah_halaman = int(input("Masukkan jumlah halaman buku: "))
            perpustakaan.tambah_buku(judul, penulis, jumlah_halaman)
            print("Buku berhasil ditambahkan.")
        elif pilihan == 2:
            perpustakaan.edit()
        elif pilihan == 3:
            perpustakaan.cari_buku()
        elif pilihan == 4:
            perpustakaan.hapus()
        elif pilihan == 5:  
            perpustakaan.tampilkan_semua_buku()
        elif pilihan == 6:
            print("Terima kasih telah menggunakan layanan perpustakaan.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

main()

#edit, delete, pencarian
