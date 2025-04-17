class mahasiswa:
    def __init__(self, nama, nim, prodi, alamat):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.alamat = alamat

    def info_mhs(self):
        print(f"Nama    : {self.nama}")
        print(f"NIM     : {self.nim}")
        print(f"Prodi   : {self.prodi}")
        print(f"Alamat  : {self.alamat}")

daftar_mahasiswa = []

for i in range(3):
    print(f"Data Mahasiswa {i + 1}")
    nama = input("Masukkan nama : ")
    nim = input("Masukkan NIM : ")
    prodi = input("Masukkan Program Studi : ")
    alamat = input("Masukkan alamat : ")

    mhs = mahasiswa(nama, nim, prodi, alamat)
    daftar_mahasiswa.append(mhs)
    print("-------------------")

print("\n-------------------")
print("INFORMASI MAHASISWA")
print("-------------------")
for mhs in daftar_mahasiswa:
    mhs.info_mhs()
    print("-------------------")
