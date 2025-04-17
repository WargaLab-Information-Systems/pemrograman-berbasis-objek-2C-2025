class Mahasiswa:
    def __init__(self, nama, nim, prodi, alamat):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.alamat = alamat

    def tampilkan_info(self):
        print("---DATA MAHASISWA---")
        print(f"Nama     : {self.nama}")
        print(f"NIM      : {self.nim}")
        print(f"Prodi    : {self.prodi}")
        print(f"Alamat   : {self.alamat}")

daftar_mahasiswa = []  
while True:
    n = int(input("Masukkan jumlah data mahasiswa yang ingin ditambah (min. 3): "))
    if n < 3:
        print("Jumlah data minimal adalah 3. Silakan coba lagi.")
    else:
        break

for i in range(n):
    print(f"Input data mahasiswa ke-{i+1}")
    nama = input("Masukkan Nama: ")
    nim = input("Masukkan NIM: ")
    prodi = input("Masukkan Prodi: ")
    alamat = input("Masukkan Alamat: ")

    mhs = Mahasiswa(nama, nim, prodi, alamat)
    daftar_mahasiswa.append(mhs)

print("---- DATA MAHASISWA ----")
for mahasiswa in daftar_mahasiswa:
    mahasiswa.tampilkan_info()
