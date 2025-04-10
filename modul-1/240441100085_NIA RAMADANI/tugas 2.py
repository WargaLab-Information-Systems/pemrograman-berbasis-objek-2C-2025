class Mahasiswa:
    def __init__(self, nama, nim, prodi, alamat):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.alamat = alamat

    def tampilkan_info(self):
        print("-----------")
        print(f"Nama   : {self.nama}")
        print(f"NIM    : {self.nim}")
        print(f"Prodi  : {self.prodi}")
        print(f"Alamat : {self.alamat}")
        print("-----------")

print("Input Mahasiswa 1")
nama1 = input("Masukkan nama: ")
nim1 = input("Masukkan NIM: ")
prodi1 = input("Masukkan prodi: ")
alamat1 = input("Masukkan alamat: ")
mhs1 = Mahasiswa(nama1, nim1, prodi1, alamat1)

print("\nInput Mahasiswa 2")
nama2 = input("Masukkan nama: ")
nim2 = input("Masukkan NIM: ")
prodi2 = input("Masukkan prodi: ")
alamat2 = input("Masukkan alamat: ")
mhs2 = Mahasiswa(nama2, nim2, prodi2, alamat2)

print("\nInput Mahasiswa 3")
nama3 = input("Masukkan nama: ")
nim3 = input("Masukkan NIM: ")
prodi3 = input("Masukkan prodi: ")
alamat3 = input("Masukkan alamat: ")
mhs3 = Mahasiswa(nama3, nim3, prodi3, alamat3)


print("\nData Mahasiswa:")
mhs1.tampilkan_info()
mhs2.tampilkan_info()
mhs3.tampilkan_info()
