class Mahasiswa:
    def __init__(self, nama, nim, jurusan, alamat):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.alamat = alamat
    
    def tampilkan(self):
        print(f"Nama: {self.nama}, NIM: {self.nim}, Jurusan: {self.jurusan}, Alamat: {self.alamat}")

data_mahasiswa = []

for data in range(3):
    print(f"Masukkan data Mahasiswa ke-{data+1}")
    nama = input("Masukkan nama: ")
    nim = input("Masukkan NIM: ")
    jurusan = input("Masukkan Jurusan: ")
    alamat = input("Masukkan alamat: ")
    print("-----" * 15)

    mahasiswa = Mahasiswa(nama,nim,jurusan,alamat)
    data_mahasiswa.append(mahasiswa)

print("Data Mahasiswa Saat ini")
for mahasiswa in data_mahasiswa:
    mahasiswa.tampilkan()