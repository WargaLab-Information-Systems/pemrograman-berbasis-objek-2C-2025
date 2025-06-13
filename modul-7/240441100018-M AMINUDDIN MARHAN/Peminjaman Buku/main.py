from bukufiksi import BukuFiksi
from bukureferensi import  BukuReferensi

def peminjaman(buku):
    for b in buku:
        print(b.pinjam())
        print(b.reservasi())
        print()

buku = [BukuFiksi(5), BukuReferensi(3)]
peminjaman(buku)