from reservasi import Reservasi

class Bukureferensi(Reservasi):
    def reservasi(self):
        jawab = input("masukkan judul buku referensi yang ingin anda pinjam: ")
        print (f"buku referensi dengan judul {jawab} berhasil di reservasi")