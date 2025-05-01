class mahasiswa:
    def __init__(self, nama, nim, prodi, alamat):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.alamat = alamat

    def tampilkan_info(self):
        print(f"***DATA MAHASISWA*** \nNama : {self.nama} \nNim : {self.nim} \nProdi : {self.prodi} \nAlamat : {self.alamat}")

mahasiswa1 = mahasiswa(input("Nama : "), input("Nim : "), input("Prodi : "), input("alamat : "))
mahasiswa2 = mahasiswa(input("Nama : "), input("Nim : "), input("Prodi : "), input("alamat : "))
mahasiswa3 = mahasiswa(input("Nama : "), input("Nim : "), input("Prodi : "), input("alamat : "))

print()
mahasiswa1.tampilkan_info()
print()
mahasiswa2.tampilkan_info()
print()
mahasiswa3.tampilkan_info()