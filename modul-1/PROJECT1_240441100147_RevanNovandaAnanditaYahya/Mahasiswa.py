class Mahasiswa:
    def __init__(self, nama, nim, jurusan, alamat):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.alamat = alamat

    def tampilkan_info(self):
        print(f"Nama: {self.nama}, NIM: {self.nim}, Jurusan: {self.jurusan}, Alamat: {self.alamat}")

print("Masukkan data:")
m1 = Mahasiswa(input("Nama: "), input("NIM: "), input("Jurusan/Prodi: "), input("Alamat: "))

print("\nMasukkan data:")
m2 = Mahasiswa(input("Nama: "), input("NIM: "), input("Jurusan/Prodi: "), input("Alamat: "))

print("\nMasukkan data:")
m3 = Mahasiswa(input("Nama: "), input("NIM: "), input("Jurusan/Prodi: "), input("Alamat: "))

print("\nData Mahasiswa:")
m1.tampilkan_info()
m2.tampilkan_info()
m3.tampilkan_info()