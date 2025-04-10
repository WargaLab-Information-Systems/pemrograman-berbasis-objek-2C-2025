class Mahasiswa:
    def __init__(self, nama, nim, jurusan, alamat):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.alamat = alamat

    def info_mahasiswa(self):
        print("============================")
        print(f"Nama     : {self.nama}")
        print(f"NIM      : {self.nim}")
        print(f"Jurusan  : {self.jurusan}")
        print(f"Alamat   : {self.alamat}")
        print("============================")

mahasiswa_list = []

for i in range(3):
    print(f"Masukkan data mahasiswa ke-{i+1}:")
    nama = input("Nama: ")
    nim = input("NIM: ")
    jurusan = input("Jurusan/Prodi: ")
    alamat = input("Alamat: ")
    
    mahasiswa = Mahasiswa(nama, nim, jurusan, alamat)
    mahasiswa_list.append(mahasiswa)
print("\nData Mahasiswa:")
for mhs in mahasiswa_list:
    mhs.info_mahasiswa()