from books.buku_fiksi import BukuFiksi
from books.buku_referensi import BukuReferensi
from services.manajemen_buku import ManajemenBuku

def main():
    judul_fiksi = input("Masukkan judul buku fiksi: ")
    penulis_fiksi = input("Masukkan nama penulis buku fiksi: ")
    fiksi = BukuFiksi(judul_fiksi, penulis_fiksi)

    judul_referensi = input("Masukkan judul buku referensi: ")
    penulis_referensi = input("Masukkan nama penulis buku referensi: ")
    referensi = BukuReferensi(judul_referensi, penulis_referensi)

    manajemen = ManajemenBuku()
    manajemen.tambah_buku(fiksi)
    manajemen.tambah_buku(referensi)

    print("\n== Daftar Buku ==")
    manajemen.tampilkan_semua()

    print("\n== Aksi pada Buku Fiksi ==")
    print("Pilihan aksi: ")
    print("1. Pinjam")
    print("2. Kembalikan")
    print("3. Reservasi")
    aksi_fiksi = input("Masukkan pilihan aksi (1/2/3): ")

    if aksi_fiksi == "1":
        fiksi.pinjam()
    elif aksi_fiksi == "2":
        fiksi.kembalikan()
    elif aksi_fiksi == "3":
        fiksi.reservasi()
    else:
        print("Pilihan aksi tidak valid untuk buku fiksi.")

    # Aksi terhadap buku referensi
    print("\n== Aksi pada Buku Referensi ==")
    print("Pilihan aksi: ")
    print("1. Reservasi")
    print("2. Batalkan Reservasi")
    aksi_referensi = input("Masukkan pilihan aksi (1/2): ")

    if aksi_referensi == "1":
        referensi.reservasi()
    elif aksi_referensi == "2":
        referensi.batalkan_reservasi()
    else:
        print("Pilihan aksi tidak valid untuk buku referensi.")

if __name__ == "__main__":
    main()