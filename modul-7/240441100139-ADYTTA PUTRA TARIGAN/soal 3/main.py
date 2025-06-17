from fiksi import BukuFiksi
from referensi import BukuReferensi
from manajemen_peminjaman import ManajemenPeminjaman

def tampilkan_menu():
    print("""
1. Tambah Buku
2. Lihat Semua Buku
3. Pinjam Buku Fiksi
4. Kembalikan Buku Fiksi
5. Reservasi Buku
6. Batalkan Reservasi
0. Keluar
""")

def main():
    manajemen = ManajemenPeminjaman()

    while True:
        tampilkan_menu()
        try:
            pilihan = int(input("Pilih menu: "))
        except ValueError:
            print("Masukkan angka yang valid.")
            continue

        if pilihan == 1:
            print("\nJenis Buku:\n1. Fiksi\n2. Referensi")
            jenis = int(input("Pilih jenis buku (1/2): "))
            if jenis not in [1, 2]:
                print("Pilihan jenis buku tidak valid.")
                continue

            judul = input("Judul Buku: ")
            penulis = input("Penulis: ")

            if jenis == 1:
                buku = BukuFiksi(judul, penulis)
            else:
                buku = BukuReferensi(judul, penulis)

            manajemen.tambah_buku(buku)
            print("Buku berhasil ditambahkan.")

        elif pilihan == 2:
            print("\nDaftar Buku:")
            manajemen.tampilkan_semua_buku()

        elif pilihan == 3:
            manajemen.tampilkan_semua_buku()
            try:
                idx = int(input("Masukkan nomor buku yang ingin dipinjam: ")) - 1
                buku = manajemen.ambil_buku(idx)
                if isinstance(buku, BukuFiksi):
                    buku.pinjam()
                else:
                    print("Buku ini tidak bisa dipinjam.")
            except:
                print("Indeks tidak valid.")

        elif pilihan == 4:
            manajemen.tampilkan_semua_buku()
            try:
                idx = int(input("Masukkan nomor buku yang ingin dikembalikan: ")) - 1
                buku = manajemen.ambil_buku(idx)
                if isinstance(buku, BukuFiksi):
                    buku.kembalikan()
                else:
                    print("Buku ini tidak bisa dikembalikan.")
            except:
                print("Indeks tidak valid.")

        elif pilihan == 5:
            manajemen.tampilkan_semua_buku()
            try:
                idx = int(input("Masukkan nomor buku untuk reservasi: ")) - 1
                buku = manajemen.ambil_buku(idx)
                buku.reservasi()
            except:
                print("Indeks atau aksi tidak valid.")

        elif pilihan == 6:
            manajemen.tampilkan_semua_buku()
            try:
                idx = int(input("Masukkan nomor buku untuk batal reservasi: ")) - 1
                buku = manajemen.ambil_buku(idx)
                buku.batal_reservasi()
            except:
                print("Indeks atau aksi tidak valid.")

        elif pilihan == 0:
            print("Terima kasih!")
            break

        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
