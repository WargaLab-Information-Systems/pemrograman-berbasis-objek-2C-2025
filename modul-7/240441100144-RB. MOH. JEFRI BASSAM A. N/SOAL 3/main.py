from bukuPelajaran import BukuPelajaran
from novel import Novel
from komik import Komik

while True:
    print("\n==== SISTEM PEMINJAMAN BUKU UJEE ====")
    nama = input("Masukkan nama peminjam : ")

    print("--- Pilih jenis buku ---")
    print("1. Buku Pelajaran")
    print("2. Novel")
    print("3. Komik")
    pilihan = int(input("Pilihan (1/2/3): "))

    if pilihan == 1:
        buku = BukuPelajaran()
    elif pilihan == 2:
        buku = Novel()
    elif pilihan == 3:
        buku = Komik()
    else:
        print("\n-- Pilihan tidak valid --")
        continue
        
    buku.info_buku()
    lama = int(input("\nMasukkan lama pinjam (hari) : "))
    denda = buku.hitung_denda(lama)

    print("\n--- detail peminjaman ---")
    print(f"Nama Peminjam   : {nama}")
    print(f"Jenis Buku      : {buku.jenis}")
    print(f"Lama Pinjam     : {lama} hari")
    print(f"Denda Terlambat : Rp{denda}")

    ulang = input("\nMau ngulang? (y/n): ")
    if ulang != 'y':
        print("\n-- Program selesai --")
        print()
        break