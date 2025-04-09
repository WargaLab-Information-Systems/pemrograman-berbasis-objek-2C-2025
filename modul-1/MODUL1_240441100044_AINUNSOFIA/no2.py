class Mahasiswa: #class
    def __init__(self, nama, nim, jurusan, alamat): #constructor
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.alamat = alamat

    def info_mahasiswa(self): #method
        return f"Nama: {self.nama}, NIM: {self.nim}, Jurusan: {self.jurusan}, Alamat: {self.alamat}"

#membuat fungsi untuk meminta input data mahasiswa
def data_mahasiswa():
    nama = input("Masukkan nama: ")
    nim = input("Masukkan NIM: ")
    jurusan = input("Masukkan jurusan/prodi: ")
    alamat = input("Masukkan alamat: ")
    return Mahasiswa(nama, nim, jurusan, alamat)

#membuat list untuk menyimpan data mahasiswa
mahasiswa_list = []
for i in range(3):
    print(f"\nData Mahasiswa ke-{i + 1}:")
    mahasiswa = data_mahasiswa()
    mahasiswa_list.append(mahasiswa)

#menampilkan hasil
print("\nInformasi Mahasiswa:")
for mhs in mahasiswa_list:
    print(mhs.info_mahasiswa())