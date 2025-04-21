class mahasiswa:
    def __init__(self, nama, nim, jurusan, alamat):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.alamat = alamat
        
    def tampilkan_mahasiswa(self):
        print(f"Nama : {self.nama}")
        print(f"Nim : {self.nim}")
        print(f"Jurusan : {self.jurusan}")
        print(f"Alamat : {self.alamat}")
        print("=" * 30)
        
print("Mahasiswa 1") 
mahasiswa1 = mahasiswa(input("Masukkan nama mahasiswa : "),
                       input("Masukkan NIM mahasiswa : "),
                       input("Masukkan jurusan/prodi mahasiswa : "),
                       input("Masukkan alamat mahasiswa : "))

print("\nMahasiswa 2")
mahasiswa2 = mahasiswa(input("Masukkan nama mahasiswa : "),
                       input("Masukkan NIM mahasiswa : "),
                       input("Masukkan jurusan/prodi mahasiswa : "),
                       input("Masukkan alamat mahasiswa : "))

print("\nMahasiswa 3")
mahasiswa3 = mahasiswa(input("Masukkan nama mahasiswa : "),
                       input("Masukkan NIM mahasiswa : "),
                       input("Masukkan jurusan/prodi mahasiswa : "),
                       input("Masukkan alamat mahasiswa : "))

print("\nInformasi Mahasiswa:")
mahasiswa1.tampilkan_mahasiswa()

print("\nInformasi Mahasiswa:")
mahasiswa2.tampilkan_mahasiswa()

print("\nInformasi Mahasiswa:")
mahasiswa3.tampilkan_mahasiswa()
