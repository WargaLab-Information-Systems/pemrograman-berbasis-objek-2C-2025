class mahasiswa:
    def __init__(self, nama, nim, prodi,alamat):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.alamat = alamat

    def tampilkan_data(self):
        print("=== DATA MAHASISWA ===")
        print(f"Nama : {self.nama}")
        print(f"NIM : {self.nim}")
        print(f"Prodi : {self.prodi}")
        print(f"Alamat : {self.alamat}")
        print(" ")

mahasiswa_list = []
for i in range(3):
    print(f"Masukkan data mahasiswa ke-{i+1}")
    nama = input("Masukkan Nama : ")
    nim = input("Masukkan NIM : ")
    prodi = input("Masukkan Prodi : ")
    alamat = input("Masukkan Alamat : ")

    mahasiswa1 = mahasiswa(nama, nim, prodi, alamat)
    mahasiswa_list.append(mahasiswa1)

for mhs in mahasiswa_list:
    mhs.tampilkan_data()