from buku_fiksi import BukuFiksi
from buku_referensi import BukuReferensi

def main():
    while True:
        print("Selamat datang di toko buku")
        print("Jenis Buku:")
        print("1. Buku Fiksi")
        print("2. Buku Referensi")
    
        pilihan = int(input("Pilih jenis buku (1/2): "))
    
        if pilihan == 1:
            nama = input("Masukkan nama anda: ")
            buku = BukuFiksi()
        elif pilihan == 2:
            nama = input("Masukkan nama anda: ")
            buku = BukuReferensi()
        else:
            print("Pilihan tidak valid")
            exit()
    
        print("1. Pinjam")
        print("2. Reservasi")
        aksi = int(input("Pilih (1/2): "))
    
        if aksi == 1:
            buku.pinjam(nama)
        elif aksi == 2:
            buku.reservasi(nama)
        else:
            print("Pilihan tidak valid")
            exit()
        
        n = input("Ingin meminjam buku lagi (y/n): ")
        if n != "y":
            break
main()