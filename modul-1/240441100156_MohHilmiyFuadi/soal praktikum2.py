# class Mahasiswa:
#     def __init__(self, nama, nim, jurusan, alamat):
#         self.nama = nama
#         self.nim = nim
#         self.jurusan = jurusan
#         self.alamat = alamat

#     def info(self):
#         return f"Nama: {self.nama}, NIM: {self.nim}, Jurusan: {self.jurusan}, Alamat: {self.alamat}"

# def main():
#     mahasiswa_list = []

#     # Mengambil input dari pengguna untuk 3 mahasiswa
#     for i in range(3):
#         print(f"\nMasukkan data mahasiswa ke-{i + 1}:")
#         nama = input("Nama: ")
#         nim = input("NIM: ")
#         jurusan = input("Jurusan/Prodi: ")
#         alamat = input("Alamat: ")

#         # Membuat objek Mahasiswa dan menambahkannya ke dalam daftar
#         mahasiswa = Mahasiswa(nama, nim, jurusan, alamat)
#         mahasiswa_list.append(mahasiswa)

#     # Menampilkan informasi semua mahasiswa
#     print("\nData Mahasiswa:")
#     for mhs in mahasiswa_list:
#         print(mhs.info())


# if __name__ == "__main__":
#     main()
class dosen:
    def __init__(self,nama,nip):
        self.nama = nama
        self.nip = nip

    def info(self):
        return f"nama: {nama}, nip: {nip}"
    
    def main():
        dosen_list = []
    
    for i in range(3):
        print (f"Masaukan data Dosen ke-{i + 1}:")
        nama = input ("Nama :")
        nip = input ("Nip:")

        dosen = dosen(nama,nip)
        dosen_list.append(dosen)