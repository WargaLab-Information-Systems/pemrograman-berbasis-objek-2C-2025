class Mahasiswa:
    def __init__(self, nama, nim, jurusan, alamat):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.alamat = alamat
    
    def tampilkan_info(self):
        print(f"  Nama    : {self.nama}")
        print(f"  NIM     : {self.nim}")
        print(f"  Jurusan : {self.jurusan}")
        print(f"  Alamat  : {self.alamat}")
        print("-" * 30)

mahasiswa_list = []
for i in range(3):
    print(f"\nInput data mahasiswa ke-{i+1}")
    print("-" * 30)
    nama = input("Masukkan nama mahasiswa: ")
    nim = input("Masukkan NIM mahasiswa: ")
    jurusan = input("Masukkan jurusan mahasiswa: ")
    alamat = input("Masukkan alamat mahasiswa: ")
    mahasiswa_list.append(Mahasiswa(nama, nim, jurusan, alamat))

for mahasiswa in mahasiswa_list:
    mahasiswa.tampilkan_info()
