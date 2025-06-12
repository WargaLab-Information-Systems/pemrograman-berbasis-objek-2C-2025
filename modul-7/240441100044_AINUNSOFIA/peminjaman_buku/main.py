from buku_fiksi import BukuFiksi
from buku_referensi import BukuReferensi

def main():
    print("=== Sistem Peminjaman Buku ===")
    nama = input("Masukkan nama Anda: ")
    print("Jenis buku yang tersedia:")
    print("1. Buku Fiksi")
    print("2. Buku Referensi")
    
    pilihan = input("Pilih jenis buku (1/2): ")
    judul = input("Masukkan judul buku: ")

    if pilihan == '1':
        buku = BukuFiksi(judul)
    elif pilihan == '2':
        buku = BukuReferensi(judul)
    else:
        print("Pilihan tidak valid.")
        return

    print("\nAksi yang tersedia:")
    print("1. Pinjam")
    print("2. Reservasi")
    aksi = input("Pilih aksi (1/2): ")

    if aksi == '1':
        # Periksa apakah objek punya method `pinjam`
        if hasattr(buku, 'pinjam'):
            buku.pinjam(nama)
        else:
            print("Jenis buku ini tidak dapat dipinjam.")
    elif aksi == '2':
        buku.reservasi(nama)
    else:
        print("Aksi tidak valid.")

if __name__ == "__main__":
    main()
