# #cari buku,edit buku,delete buku,judulsama tapi isinya beda bisa diedit
class Buku:
    def __init__(self, judul, penulis, jumlah_halaman):
        self.__judul = judul
        self.__penulis = penulis
        self.__jumlah_halaman = jumlah_halaman

    @property
    def judul(self):
        return self.__judul
    @judul.setter
    def judul(self, judul):
        self.__judul = judul

    @property
    def penulis(self):
        return self.__penulis
    @penulis.setter
    def penulis(self, penulis):
        self.__penulis = penulis

    @property
    def jumlah_halaman(self):
        return self.__jumlah_halaman
    @jumlah_halaman.setter
    def jumlah_halaman(self, jumlah_halaman):
        self.__jumlah_halaman = jumlah_halaman

    def __str__(self):
        return f"Judul: {self.__judul}, Penulis: {self.__penulis}, Jumlah Halaman: {self.__jumlah_halaman}"

class Perpustakaan:
    def __init__(self):
        self.buku_list = []

    def tambah_buku(self, buku):
        self.buku_list.append(buku)

    def tampilkan_buku(self):
        if not self.buku_list:
            print("Belum ada buku di perpustakaan.")
        else:
            for buku in self.buku_list:
                print(buku)

    def cari_buku(self, judul):
        return [(i, buku) for i, buku in enumerate(self.buku_list) if buku.judul.lower() == judul.lower()]

if __name__ == "__main__":
    perpustakaan = Perpustakaan()

    while True:
        print("\nMenu")
        print("1. Tambah Buku")
        print("2. Lihat Semua Buku")
        print("3. Cari Buku")
        print("4. Edit Buku")
        print("5. Delete Buku")
        print("6. Keluar")
        pilihan = input("Pilih 1/2/3/4/5/6: ")

        if pilihan == '1':
            judul = input("Masukkan judul buku: ")
            penulis = input("Masukkan nama penulis: ")
            while True:
                jumlah_input = input("Masukkan jumlah halaman: ")
                if jumlah_input.isdigit():
                    jumlah_halaman = int(jumlah_input)
                    break
                else:
                    print("Harus angka")
            perpustakaan.tambah_buku(Buku(judul, penulis, jumlah_halaman))
            print(f"Buku '{judul}' telah ditambahkan ke perpustakaan")

        elif pilihan == '2':
            print("Daftar Buku di Perpustakaan:")
            perpustakaan.tampilkan_buku()

        elif pilihan == '3':
            judul_cari = input("Masukkan judul buku yang dicari: ")
            hasil = perpustakaan.cari_buku(judul_cari)
            if hasil:
                print("Buku ditemukan:")
                for i, (idx, buku) in enumerate(hasil, 1):
                    print(f"{i}. {buku}")
            else:
                print("Buku tidak ditemukan")

        elif pilihan == '4':
            judul_cari = input("Masukkan judul buku yang ingin diedit: ")
            hasil = perpustakaan.cari_buku(judul_cari)
            if hasil:
                idx_buku = hasil[0][0]  
                buku = perpustakaan.buku_list[idx_buku]
                print(f"Mengedit buku: {buku}")
                
                buku.penulis = input("Penulis baru: ")
                while True:
                    jumlah_baru = input("Jumlah halaman baru: ")
                    if jumlah_baru.isdigit(): 
                        buku.jumlah_halaman = int(jumlah_baru)
                        break
                    else:
                        print("Masukkan angka yang sesuai")
                print("Buku berhasil diedit")
            else:
                print("Buku tidak ditemukan")

        elif pilihan == '5':
            judul_hapus = input("Masukkan judul buku yang ingin dihapus: ")
            hasil = perpustakaan.cari_buku(judul_hapus)
            if hasil:
                idx_asli = hasil[0][0] 
                hapus_buku = perpustakaan.buku_list.pop(idx_asli)
                print(f"Buku '{hapus_buku.judul}' telah dihapus")
            else:
                print("Buku tidak ditemukan")

        elif pilihan == "6":
            print("Terima kasih telah menggunakan layanan kami")
            break
        else:
            print("Pilihan tidak valid")