class Mahasiswa:
    def __init__(self, nama, nim, jurusan, alamat):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.alamat = alamat 

    def tampilkan_info(self):
        print("========== Data Mahasiswa ==========")
        print(f"Nama    : {self.nama}")
        print(f"NIM     : {self.nim}")
        print(f"Jurusan : {self.jurusan}")
        print(f"Alamat  : {self.alamat}")
        print("====================================\n")


mahasiswa_list = []

for i in range(3):
    print(f"\nMasukkan data mahasiswa ke-{i+1}:")
    nama = input("Nama    : ")
    nim = input("NIM     : ")
    jurusan = input("Jurusan : ")
    alamat = input("Alamat  : ")
    mahasiswa_list.append(Mahasiswa(nama, nim, jurusan, alamat))

print("\n=== Daftar Mahasiswa ===\n")
for mahasiswa in mahasiswa_list:
    mahasiswa.tampilkan_info()
