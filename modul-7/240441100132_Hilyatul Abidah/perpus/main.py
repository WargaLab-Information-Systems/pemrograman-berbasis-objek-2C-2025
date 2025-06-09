from buku_fiksi import BukuFiksi
from buku_referensi import BukuReferensi

def validasi_alfabet(teks):
    return all(kata.isalpha() for kata in teks.strip().split())

def input_dengan_validasi(prompt, field_nama):
    while True:
        nilai = input(prompt).strip()
        if validasi_alfabet(nilai):
            return nilai
        else:
            print(f"{field_nama} hanya boleh terdiri dari huruf dan spasi. Silakan coba lagi.")

def pilih_aksi(buku):
    while True:
        print(f"\nApa yang ingin Anda lakukan dengan buku '{buku.judul}'?")
        print("1. Pinjam")
        print("2. Reservasi")
        try:
            aksi = int(input("Pilih aksi (1/2): "))
        except ValueError:
            print("Masukkan angka 1 atau 2.")
            continue

        if aksi == 1:
            buku.pinjam()
            break
        elif aksi == 2:
            buku.reservasi()
            break
        else:
            print("Aksi tidak valid. Silakan pilih 1 atau 2.")

def pilih_jenis_buku():
    while True:
        print("\n=== Pilih Jenis Buku ===")
        print("1. Buku Fiksi")
        print("2. Buku Referensi")
        try:
            pilihan = int(input("Masukkan pilihan (1/2): "))
        except ValueError:
            print("Masukkan angka 1 atau 2.")
            continue

        if pilihan == 1:
            judul = input_dengan_validasi("Masukkan judul buku fiksi: ", "Judul")
            pengarang = input_dengan_validasi("Masukkan pengarang buku fiksi: ", "Pengarang")
            buku = BukuFiksi(judul, pengarang)
            pilih_aksi(buku)
            return buku
        elif pilihan == 2:
            judul = input_dengan_validasi("Masukkan judul buku referensi: ", "Judul")
            pengarang = input_dengan_validasi("Masukkan pengarang buku referensi: ", "Pengarang")
            buku = BukuReferensi(judul, pengarang)
            pilih_aksi(buku)
            return buku
        else:
            print("Pilihan tidak valid. Silakan pilih 1 atau 2.")

def main():
    while True:
        daftar_buku = []
        while True:
            buku = pilih_jenis_buku()
            daftar_buku.append(buku)
            lanjut = input("Ingin tambah buku lain? (y/n): ").lower()
            if lanjut != 'y':
                break
        
        print("\n=== Ringkasan Buku ===")
        for buku in daftar_buku:
            buku.info()

        ulang = input("\nIngin melakukan transaksi baru? (y/n): ").lower()
        if ulang != 'y':
            print("Terima kasih telah menggunakan sistem perpustakaan!")
            break

if __name__ == "__main__":
    main()
