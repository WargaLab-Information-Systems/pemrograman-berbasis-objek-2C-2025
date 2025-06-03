class Mahasiswa:
    def __init__(self, nama, nim, prodi, alamat):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.alamat = alamat

    def tampilkan_info(self):
        print(f"Nama   : {self.nama}")
        print(f"NIM    : {self.nim}") 
        print(f"Prodi  : {self.prodi}") 
        print(f"Alamat : {self.alamat}")  

daftar_mahasiswa = []

for i in range(3):
    print(f"Masuskkan data mahasiswa ke-{i+1}")
    nama = input("Nama  :")
    nim = input("NIM  :")
    prodi = input("Prodi  :")
    alamat = input("Alamat  :")

    mhs = Mahasiswa(nama, nim, prodi, alamat)
    daftar_mahasiswa.append(mhs)

print("\nData Mahasiswa:")
for mhs in daftar_mahasiswa:
    mhs.tampilkan_info() 