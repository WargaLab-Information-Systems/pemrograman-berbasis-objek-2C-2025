from buku_fiksi import BukuFiksi
from buku_referensi import BukuReferensi
from interface_peminjaman import SistemPeminjaman
from interface_reservasi import SistemReservasi

def tambah_buku():
    judul = input("Masukkan judul buku: ")
    penulis = input("Masukkan penulis buku: ")
    tipe = input("Tipe buku (Fiksi/Referensi): ").strip().lower()
    
    if tipe == "fiksi":
        return BukuFiksi(judul, penulis)
    elif tipe == "referensi":
        return BukuReferensi(judul, penulis)
    else:
        print("Tipe buku tidak valid, default ke Fiksi.")
        return BukuFiksi(judul, penulis)

def pilih_buku(daftar_buku):
    if not daftar_buku:
        print("Belum ada buku yang tersedia.")
        return None

    print("\nDaftar Buku:")
    for i, buku in enumerate(daftar_buku, 1):
        print(f"{i}. {buku.judul} ({buku.tipe_buku()}) oleh {buku.penulis}")
    pilih = input("Pilih nomor buku: ")

    if pilih.isdigit() and 1 <= int(pilih) <= len(daftar_buku):
        return daftar_buku[int(pilih) - 1]
    else:
        print("Pilihan tidak valid.")
        return None

def main():
    daftar_buku = []
    peminjaman = SistemPeminjaman()
    reservasi = SistemReservasi()

    while True:
        print("\nMenu:")
        print("1. Tambah buku")
        print("2. Pinjam buku")
        print("3. Reservasi buku")
        print("4. Tampilkan semua buku")
        print("0. Keluar")

        pilihan = int(input("Pilih menu: "))

        if pilihan == 1:
            buku = tambah_buku()
            daftar_buku.append(buku)
            print(f"Buku '{buku.judul}' berhasil ditambahkan.")
        elif pilihan == 2:
            buku = pilih_buku(daftar_buku)
            if buku:
                hasil = peminjaman.pinjam(buku)
                print(hasil)
        elif pilihan == 3:
            buku = pilih_buku(daftar_buku)
            if buku:
                hasil = reservasi.reservasi(buku)
                print(hasil)
        elif pilihan == 4:
            if daftar_buku:
                print("\nDaftar Buku Saat Ini:")
                for buku in daftar_buku:
                    print(f"- {buku.judul} ({buku.tipe_buku()}) ditulis oleh {buku.penulis}")
            else:
                print("Belum ada buku yang tersedia.")
        elif pilihan == 0:
            print("Terima kasih. Sistem selesai.")
            break
        else:
            print("Pilihan menu tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
