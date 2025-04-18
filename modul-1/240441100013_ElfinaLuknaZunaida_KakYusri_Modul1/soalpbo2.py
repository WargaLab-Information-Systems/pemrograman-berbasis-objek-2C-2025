class mahasiswa:
    def __init__ (self, nama, nim, prodi, alamat):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.alamat = alamat

    def tampilkan_info(self):
        print(f"\n=== Data Mahasiswa ===:")
        print(f"Nama    : {self.nama}")
        print(f"Nim     : {self.nim}")
        print(f"Prodi   : {self.prodi}")
        print(f"Alamat  : {self.alamat}")

data_mahasiswa = []

for i in range(3):
    print(f"Masukkan Data Mahasiswa ke:{i+1}")
    nama = input("Nama:")
    nim = input("Nim:")
    prodi = input("Prodi:")
    alamat = input ("alamat:")
  
    mhs = mahasiswa(nama, nim, prodi, alamat)
    data_mahasiswa.append (mhs)

print("\n=== Daftar Seluruh Mahasiswa ===")
for mahasiswa in data_mahasiswa:
    mahasiswa.tampilkan_info()