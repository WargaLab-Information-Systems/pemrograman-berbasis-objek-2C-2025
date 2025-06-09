from bukuFiksi import BukuFiksi
from bukuReferensi import BukuReferensi

def main():
    print("Selamat datang di sistem peminjaman buku")
    print("1. Buku Fiksi")
    print("2. Buku Referensi")

    pilihan = int(input("Pilih jenis buku (1/2): "))
    nama = input("Masukkan nama Anda: ")
    judul = input("Masukkan judul buku: ")

    if pilihan == 1:
        buku = BukuFiksi(judul)
    elif pilihan == 2:
        buku = BukuReferensi(judul)
    else:
        print("Pilihan tidak valid.")

    print("\n--- Hasil ---")
    print(buku.pinjam(nama))
    print(buku.reservasi(nama))

main()