from buku_fiksi import Bukufiksi
from buku_referensi import Bukureferensi

simpandata = []
while True:
    print("\nSELAMAT DATANG DI PERPUSTAKAAN")
    print("1. Peminjaman buku fiksi")
    print("2. Peminjaman referensi")
    print("3. Tampilkan info")
    print("4. Keluar")
    jawab = int(input("masukkan nomor inputan: "))
    if jawab == 1:
        tampil = Bukufiksi()
        tampil.pinjaman()
        tampil.kembalikan()
        simpandata.append(f"Buku fiksi dengan judul {tampil.judul}")
    elif jawab == 2:
        tampil = Bukureferensi()
        tampil.reservasi()
        simpandata.append(f"Buku referensi dengan judul{tampil.judul}")
    elif jawab == 3:
        if not simpandata:
            print("belum ada data yang tersimpan")
        else:
            print("\ndaftar buku yang sedang diproses: ")
            for i, data in enumerate(simpandata, start=1):
                print(f"{i}. {data}")
    elif jawab == 4:
        print("Terimaksih sudah berkunjung")
        break
    else:
        print("inputan invalid")
